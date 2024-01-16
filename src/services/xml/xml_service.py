import os
import xml.etree.ElementTree as ET
from src.services.logger.logger_service import LoggerService
from src.services.folder.folder_service import FolderService

class XMLService:
  def __init__(self):
    self.logger = LoggerService(XMLService.__name__)
    self.folder_service = FolderService()
    self.IMPORT_PATH = os.path.abspath('import')

  def open(self, path):
    try:
      tree = ET.parse(path)
      return tree.getroot()
    except Exception as err:
      self.logger.err(f'Помилка відкриття xml файлу - {path}')
      self.logger.err(err)
  
  def parse_xml(self, xml_file, column_name):
    res = []
    for obj in xml_file.findall('.//object'):
      value = obj.find(column_name).text
      res.append(value)
    return res
  
  def find_value_count_and_change(self, xml_file, column_name, old_value, new_value):
    for obj in xml_file.findall('.//object'):
      name = obj.find(column_name)
      if name is not None and name.text == old_value:
        name.text = new_value
    return xml_file
  
  def save(self, xml_root, file_path):
    """
    Зберігає XML файл за вказаним шляхом.
    :param xml_root: Кореневий елемент XML дерева
    param file_path: Шлях для збереження XML файлу
    """
    tree = ET.ElementTree(xml_root)
    tree.write(file_path, encoding='utf-8', xml_declaration=True)


  def parsing_name_and_id_lables_and_change_it(self):
    self.logger.info('Початок вибірки назв та id з xml')
    all_files_paths = self.folder_service.get_all_file_paths(os.path.join(self.IMPORT_PATH, 'xml'))
    xml_files_paths = self.folder_service.filter_files_path_by_extension(all_files_paths, 'xml')
    all_value = []
    for xml_file_path in xml_files_paths:
      xml_file = self.open(xml_file_path)
      values = self.parse_xml(xml_file, 'name')
      all_value.extend(values)
    unique_names = list(set(all_value))
    print(unique_names)
    # for xml_file_path in xml_files_paths:
    #   xml_file = self.open(xml_file_path)
    #   new_xml_file = self.find_value_count_and_change(xml_file, 'name', '', '')
    #   self.save(new_xml_file, xml_file_path)



    
    