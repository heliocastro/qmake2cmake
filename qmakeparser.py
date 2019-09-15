class QmakeParser(object):
    """Parse a qmake file and store a map
    """

    cmakeparsed = {}

    def __init__(self, qmakefile):
        self.qmakefile = qmakefile
        self.tokens = {
            "TEMPLATE": self.template,
            "SOURCES": self.sources,
            "FORMS": self.forms,
            "RESOURCES": self.resources,
            "TRANSLATIONS": self.translations,
            "TARGET": self.target
        }

    def parse(self):
        snippet = []
        for line in self.qmakefile:
            result = line.replace('\\', '').strip()
            if len(result):
                snippet.append(result)
            else:
                continue
            if '\\' in line:
                continue
            else:
                for token in self.tokens.keys():
                    if snippet[0].lstrip().startswith(token):
                        self.tokens[token](snippet)
                snippet.clear()

    def template(self, codesnippet):
        print(codesnippet)

    def sources(self, codesnippet):
        print(codesnippet)

    def forms(self, codesnippet):
        print(codesnippet)

    def resources(self, codesnippet):
        print(codesnippet)

    def translations(self, codesnippet):
        print(codesnippet)

    def target(self, codesnippet):
        print(codesnippet)
