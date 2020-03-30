import wpf

from System.Windows import Application, Window

class MyWindow(Window):
    def __init__(self):
        wpf.LoadComponent(self, 'wpf_xaml_ipy.xaml')

if __name__ == '__main__':
    win = MyWindow()
    win.ShowDialog()
