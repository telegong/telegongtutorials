import wpf

from System.Windows import Application, Window

class MyWindow(Window):
    def __init__(self):
        wpf.LoadComponent(self, 'wpf_xaml_ipy.xaml')

if __name__ == '__main__':
    Application().Run(Window())
    #win = MyWindow()
    #app = Application()
    #app.Run(win)