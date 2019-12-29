import sys

class ProgressBar(object):
    def __init__(self, msg, width=20, pSym=u'▣ ', eSym=u'□ '):
        self.width = width

        if self.width < 0:
            self.width = 0

        self.msg = msg
        self.pSym = pSym
        self.eSym = eSym

    def update(self, p):
        total = self.width
        fill = int(round(p / (100 / float(total))))
        empty = total - fill

        pBar = self.pSym * fill + self.eSym * empty

        if not self.msg:
            self.msg = u''

        if p >= 99:
            p = 100
        pMsg = u'\r{0}{1}{2:02d}%'.format(self.msg, pBar, p)

        sys.stdout.write(pMsg)
        sys.stdout.flush()

    def calcUpdate(self, done, total):
        p = int(round((done / float(total)) * 100))
        self.update(p)
