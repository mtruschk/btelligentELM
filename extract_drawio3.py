import csv
import os
import xml.etree.ElementTree as ET
import yaml
import subprocess
import pandas as pd
import pandasql as ps

def extract_information(xml_path, base_name):
    try:
        # Parse the XML file
        tree = ET.parse(xml_path)
        root = tree.getroot()
   
    except (ET.ParseError, FileNotFoundError) as e:
        print(f"Error reading the XML file: {e}")
        return [], []

    # Lists to store data
    shapes = []
    connections = []

    # Iterate through UserObjects and mxCells
    for user_object in root.findall('.//UserObject') + root.findall('.//object'):
        adapttype = user_object.get('btelligentADAPTType')
        label = user_object.get('label')
        shape_id = user_object.get('id')

        # Determine if this is a shape or a connection
        if adapttype and adapttype in ["Dimension", "LoosePrecedence", "StrictPrecedence", "Hierarchy", "DimensionMember", "DimensionScope", "Function", "HierarchyLevel", "Attribute", "MeasureGroup", "MeasureDimension", "Hub", "Link", "Satellite", "Hub-to-Sat", "Hub-to-Link-N", "Hub-to-Link-1"]:
            mx_cell = user_object.find('./mxCell')
            
            if mx_cell.get('edge') == '1':  # It's a connection
                source = mx_cell.get('source')
                target = mx_cell.get('target')
                style = mx_cell.get('style')
                start_arrow = extract_style_value(style, 'startArrow')
                end_arrow = extract_style_value(style, 'endArrow')
                
                connection_info = {
                    'base_name': base_name,
                    'shape_id': shape_id,
                    'label': label,
                    'source': source,
                    'target': target,
                    'adapttype': adapttype,
                    'start_arrow': start_arrow,
                    'end_arrow': end_arrow
                }
                connections.append(connection_info)
            else:  # It's a shape
                shape_info = {
                    'base_name': base_name,
                    'shape_id': shape_id,
                    'label': label,
                    'adapttype': adapttype
                }
                shapes.append(shape_info)
                
    print('------------------------------------------------------\n')
                
    if len(shapes) == 0:
        shape_info = {
            'base_name': base_name,
            'shape_id': 'none',
            'label': 'none',
            'adapttype': 'none'
        }
        shapes.append(shape_info)
        print('shapes dummy added')
        
    if len(connections) == 0:  
        connection_info = {
            'base_name': base_name,
            'shape_id': 'none',
            'label': 'none',
            'source': 'none',
            'target': 'none',
            'adapttype': 'none',
            'start_arrow': 'none',
            'end_arrow': 'none'
        }
        connections.append(connection_info)
        print('connections dummy added')

    df_shapes = pd.DataFrame(shapes)
    df_connections = pd.DataFrame(connections)
        
    print(len(connections))
    if len(connections) > 0:
        sqlc = """
        SELECT c.base_name
             , c.base_name ||'.'|| c.shape_id                                               as connection_id
             , c.base_name ||'.'|| c.source                                                 as source_shape_id
             , s.adapttype                                                                  as source_type  
             , s.label                                                                      as source_label
             , c.base_name ||'.'|| c.target                                                 as target_shape_id
             , t.adapttype                                                                  as target_type  
             , t.label                                                                      as target_label
             , CASE WHEN c.source = c.target THEN 'self precedence' ELSE c.adapttype END    as connection_type
             , c.label                                                                      as connection_label
        FROM df_connections c
        JOIN df_shapes s ON s.shape_id = c.source
        JOIN df_shapes t ON t.shape_id = c.target;
        """
        
        df_connections2 = ps.sqldf(sqlc, locals())
        connections2 = df_connections2.to_dict(orient='records')
    
    print(len(shapes))    
    if len(shapes) > 0:   
        sqls = """
        SELECT s.base_name
             , s.base_name ||'.'||s.shape_id                                                as shape_id
             , s.adapttype                                                                  as shape_type
             , s.label                                                                      as label
        FROM df_shapes s;
        """
                    
        df_shapes2 = ps.sqldf(sqls, locals())
        shapes2 = df_shapes2.to_dict(orient='records')
            
    return shapes2, connections2

def extract_style_value(style, key):
    style_dict = dict(item.split('=') for item in style.split(';') if '=' in item)
    return style_dict.get(key, 'None')

def load_config(yaml_path):
    with open(yaml_path, 'r') as f:
        config = yaml.safe_load(f)
    return config

def export_drawio_to_png(drawio_executable, input_file, output_file):
    output_dir = os.path.dirname(output_file)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    command = [
        drawio_executable, 
        "--export", 
        "--format", "png", 
        "--output", output_file, 
        input_file
    ]

    try:
        subprocess.run(command, check=True)
        print(f"Export successful: {output_file}")
    except subprocess.CalledProcessError as e:
        print(f"Export error: {e}")

def to_markdown_file(xml_path, shapes, connections):
    base_name = os.path.splitext(xml_path)[0]
    md_filename = f"{base_name}.md"
    diagram_name = os.path.splitext(os.path.basename(xml_path))[0]

    with open(md_filename, 'w') as md_file:
        md_file.write(f"# Overview for Diagram **{diagram_name}**:\n\n")
        
        md_file.write(f"![Diagram {diagram_name}](../png/{diagram_name}.png)\n")
        
        md_file.write(f"## recognized shapes from b.telligent ADAPT library:\n\n")
        md_file.write(f"|Shape ID|Shape Type|Label|\n")
        md_file.write(f"|--------|----------|-----|\n")
        
        for shape in shapes:
            md_file.write(f"|{shape['shape_id']}|{shape['shape_type']}|{shape['label']}|\n")
        
        md_file.write(f"\n## recognized connections from b.telligent ADAPT library:\n\n")
        md_file.write(f"|Source Type|Source Label|Connection Type|Label|Target Type|Target Label|Connection ID|Source ID|Target ID|\n")
        md_file.write(f"|-----------|------------|---------------|-----|-----------|------------|-------------|---------|---------|\n")
        
        for connection in connections:
            md_file.write(f"|{connection['source_type']}|{connection['source_label']}|{connection['connection_type']}|{connection['connection_label']}|{connection['target_type']}|{connection['target_label']}|{connection['connection_id']}|{connection['source_shape_id']}|{connection['target_shape_id']}\n")
                                    
    print(f"Markdown file '{md_filename}' has been created.")

def write_shapes_to_csv(all_shapes, csv_filename):
    with open(csv_filename, mode='w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['base_name','shape_id','shape_type','label']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for shape in all_shapes:
            writer.writerow(shape)
    print(f"Shapes CSV file '{csv_filename}' has been created.")

def write_connections_to_csv(all_connections, csv_filename):
    with open(csv_filename, mode='w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['base_name','source_type','source_label','connection_type','connection_label','target_type','target_label','connection_id','source_shape_id','target_shape_id']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for connection in all_connections:
            writer.writerow(connection)
    print(f"Connections CSV file '{csv_filename}' has been created.")

def main():
    print('#####################################################################################################\n')
    drawio_directory = os.path.join(os.getcwd(), 'drawio')
    docs_directory = os.path.join(os.getcwd(), 'docs')
    png_directory = os.path.join(os.getcwd(), 'png')
    
    config = load_config('config.yaml')
    drawio_executable = config.get('drawio_executable_path')

    if not drawio_executable:
        print("Draw.io executable path is not set in the configuration file.")
        return

    if not os.path.exists(png_directory):
        print(f"The directory '{png_directory}' does not exist.")
        return
    if not os.path.exists(drawio_directory):
        print(f"The directory '{drawio_directory}' does not exist.")
        return
    if not os.path.exists(docs_directory):
        print(f"The directory '{docs_directory}' does not exist.")
        return

    all_shapes = []
    all_connections = []

    for root_dir, dirs, files in os.walk(drawio_directory):
        for file in files:
            if file.endswith('.drawio'):
                drawio_path = os.path.join(drawio_directory, file)
                docs_path = os.path.join(docs_directory, file)
                
                base_name = os.path.splitext(file)[0]  # Get the file name without extension
                png_path = os.path.join(png_directory, f"{base_name}.png")

                print(f"Processing file: {drawio_path}")
                print(f"PNG file: {png_path}")

                export_drawio_to_png(drawio_executable, drawio_path, png_path)

                shapes, connections = extract_information(drawio_path, base_name)
                all_shapes.extend(shapes)
                all_connections.extend(connections)

                to_markdown_file(docs_path, shapes, connections)

    # Write aggregated CSV files
    write_shapes_to_csv(all_shapes, os.path.join(docs_directory, '01_nodes.csv'))
    write_connections_to_csv(all_connections, os.path.join(docs_directory, '02_edges.csv'))

if __name__ == "__main__":
    main()