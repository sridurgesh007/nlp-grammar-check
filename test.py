import gradio as gr
from textblob import TextBlob
import language_tool_python

class SpellGrammarCheckerModule:
    def _init_(self):
        self.spell_check = TextBlob("")
        self.grammar_check = language_tool_python.LanguageTool('en-US')

    def correct_spell(self, text):
        words = text.split()
        corrected_words = []
        for word in words:
            corrected_word = str(TextBlob(word).correct())
            corrected_words.append(corrected_word)
        return " ".join(corrected_words)

    def correct_grammar(self, text):
        matches = self.grammar_check.check(text)
        found_mistakes = [match.ruleId for match in matches]
        found_mistakes_count = len(found_mistakes)
        return found_mistakes, found_mistakes_count

def spell_check(input_text):
    obj = SpellGrammarCheckerModule()
    corrected_spell_message = obj.correct_spell(input_text)
    return corrected_spell_message

def grammar_check(input_text):
    obj = SpellGrammarCheckerModule()
    grammar_mistakes, grammar_mistakes_count = obj.correct_grammar(input_text)
    return grammar_mistakes, grammar_mistakes_count

iface_spell_check = gr.Interface(fn=spell_check, inputs="text", outputs="text")
iface_grammar_check = gr.Interface(fn=grammar_check, inputs="text", outputs=["text", "text"])

iface_spell_check.launch()
iface_grammar_check.launch()