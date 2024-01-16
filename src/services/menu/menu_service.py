import inquirer
from src.services.resize_image.resize_image_service import ResizeImageService
from src.services.xml.xml_service import XMLService

class Menu:
  def __init__(self):
    self.running = True
    self.resize_image = ResizeImageService()
    self.xml_service = XMLService()
    self.menu_structure = {
      'Зміна розміру зображень': {
      'Ширина 800px': lambda: self.resize_image.height_800(),
      'Назад': None
      },
      'XML для ML': {
      'Зробити вибірку назв та id лейблів': lambda: self.xml_service.parsing_name_and_id_lables_and_change_it(),
      'Назад': None
      },
      'Вихід': None
      }

  def display_menu(self, options):
    questions = [
      inquirer.List('вибір',
                    message="Виберіть опцію",
                    choices=list(options.keys()),
                    ),
    ]
    return inquirer.prompt(questions)['вибір']

  def handle_menu(self, options):
    while True:
      choice = self.display_menu(options)
      if choice == 'Назад' or choice == 'Вихід':
        break
      action = options.get(choice)
      if action:
        action()

  def run(self):
    while self.running:
      choice = self.display_menu(self.menu_structure)
      if choice == 'Вихід':
        self.running = False
      else:
        self.handle_menu(self.menu_structure.get(choice, {}))
