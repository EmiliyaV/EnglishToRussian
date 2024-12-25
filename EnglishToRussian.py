import sublime
import sublime_plugin

class EnglishToRussianCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        print("Команда запущена")
        regions = self.view.sel()
        for region in regions:
            selected_text = self.view.substr(region)
            if selected_text.strip():
                if self.is_english(selected_text):
                    translated_text = self.translate_to_russian(selected_text)
                else:
                    translated_text = self.translate_to_english(selected_text)
                self.view.replace(edit, region, translated_text)
            else:
                print("Не выделен текст")
        sublime.message_dialog("Команда выполнена!")

    def is_english(self, text):
        english_characters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
        return any(char in english_characters for char in text)

    def translate_to_russian(self, text):
        english_to_russian = {
            'a': 'ф', 'b': 'и', 'c': 'с', 'd': 'в', 'e': 'у', 'f': 'а',
            'g': 'п', 'h': 'р', 'i': 'ш', 'j': 'о', 'k': 'л', 'l': 'д',
            'm': 'ь', 'n': 'т', 'o': 'щ', 'p': 'з', 'q': 'й', 'r': 'к',
            's': 'ы', 't': 'е', 'u': 'г', 'v': 'м', 'w': 'ц', 'x': 'ч',
            'y': 'н', 'z': 'я',
            'A': 'Ф', 'B': 'И', 'C': 'С', 'D': 'В', 'E': 'У', 'F': 'А',
            'G': 'П', 'H': 'Р', 'I': 'Ш', 'J': 'О', 'K': 'Л', 'L': 'Д',
            'M': 'Ь', 'N': 'Т', 'O': 'Щ', 'P': 'З', 'Q': 'Й', 'R': 'К',
            'S': 'Ы', 'T': 'Е', 'U': 'Г', 'V': 'М', 'W': 'Ц', 'X': 'Ч',
            'Y': 'Н', 'Z': 'Я',
        }
        return ''.join(english_to_russian.get(char, char) for char in text)

    def translate_to_english(self, text):
        russian_to_english = {
            'ф': 'a', 'и': 'b', 'с': 'c', 'в': 'd', 'у': 'e', 'а': 'f',
            'п': 'g', 'р': 'h', 'ш': 'i', 'о': 'j', 'л': 'k', 'д': 'l',
            'ь': 'm', 'т': 'n', 'щ': 'o', 'з': 'p', 'й': 'q', 'к': 'r',
            'ы': 's', 'е': 't', 'г': 'u', 'м': 'v', 'ц': 'w', 'ч': 'x',
            'н': 'y', 'я': 'z',
            'Ф': 'A', 'И': 'B', 'С': 'C', 'В': 'D', 'У': 'E', 'А': 'F',
            'П': 'G', 'Р': 'H', 'Ш': 'I', 'О': 'J', 'Л': 'K', 'Д': 'L',
            'Ь': 'M', 'Т': 'N', 'Щ': 'O', 'З': 'P', 'Й': 'Q', 'К': 'R',
            'Ы': 'S', 'Е': 'T', 'Г': 'U', 'М': 'V', 'Ц': 'W', 'Ч': 'X',
            'Н': 'Y', 'Я': 'Z',
        }
        return ''.join(russian_to_english.get(char, char) for char in text)
