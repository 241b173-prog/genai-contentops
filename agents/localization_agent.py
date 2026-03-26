class LocalizationAgent:
    def translate(self, content):
        return {
            "english": content,
            "hindi": "यह हिंदी है: " + content,
            "hinglish": "Yeh Hinglish hai: " + content
        }