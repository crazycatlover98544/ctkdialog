'''
Copyright (c) 2026 @crazycatlover98544

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

You may also read these terms at the following website: https://opensource.org/license/mit

My GitHub account is located at https://github.com/crazycatlover98544
My MistWarp account is located at https://mistwarp.org/users/crazycatlover98544

Please note that this code is not written by an expert.
I am not responsible if this harms your computer.

This is built off of "yesno.py" from my other project, "python3-powermenu-config."
'''

try:
    import tkinter as tk
    import customtkinter as ctk
except (ModuleNotFoundError,ImportError) as e:
    raise type(e)('The module(s) "tkinter" and/or "customtkinter" could not be found. Be sure you have both installed. NB: Debian repositories do not carry "customtkinter," not sure about others. Use a venv (deb package name "python3-venv").') # Needlessly complicated, but raises the same type of error that it caught.

_rv = None

def yesno(title,contents,theme='System',values=['Yes','No'],add_cancel=False):
    global _rv
    _rv = None
    
    if add_cancel:
        if values == ['Yes','No']:
            values = ['Yes','No','Cancel']
        if not len(values) == 3:
            raise ValueError('Keyword argument "values" must be a list with a length of 3 (add_cancel is True), and both items must be strings. If you want to use the default option, you do not need to pass "values."')
        elif not (type(values) == list or type(values) == tuple): # allow tuples, because they would work the same
            raise ValueError('Keyword argument "values" must be a list with a length of 2 (add_cancel is True), and both items must be strings. If you want to use the default option, you do not need to pass "values."')
    else:
        if not len(values) == 2:
            raise ValueError('Keyword argument "values" must be a list with a length of 2, and both items must be strings. If you want to use the default option, you do not need to pass "values."')
        elif not (type(values) == list or type(values) == tuple): # allow tuples, because they would work the same
            raise ValueError('Keyword argument "values" must be a list with a length of 2, and both items must be strings. If you want to use the default option, you do not need to pass "values."')
    
    root = ctk.CTk()
    root.title(title)
    root.overrideredirect(True) # Disable the window bar

    screen_width = root.winfo_screenwidth() # Get width/height to center the window
    screen_height = root.winfo_screenheight()
    root.geometry(f'250x120+{(screen_width//2)-125}+{(screen_height//2)-60}')
    
    ctk.set_appearance_mode(theme)
    
    title_ui = ctk.CTkLabel(root,text=title,font=('Arial',16))
    title_ui.pack(pady=10)
    
    contents_ui = ctk.CTkLabel(root,text=contents,font=('Arial',12))
    contents_ui.pack()
    
    def return_val(root): # Yes, I know a function inside a function is not recommended, but it works
        global _rv
        button_str = values_ui.get() # not the best name... but it works
        
        if button_str == values[0]:
            _rv = True
        elif add_cancel: # not called if "add_cancel" is False
            if button_str == values[2]:
                _rv = None
            else: # else has to be here too because otherwise, if the user selected "No," it would still return None
                _rv = False
        else:
            _rv = False
        root.quit()
        root.destroy()
    
    values_ui = ctk.CTkSegmentedButton(root,values=values,height=25,command=lambda _: return_val(root)) # likely a better way to do that, but it works
    values_ui.pack(pady=10)
    
    root.mainloop()
    
    return _rv # This is the only way to return the value, as putting return in return_val would just close the dialogue and not return anything

def yesnocancel(title,contents,theme='System',values=['Yes','No','Cancel']): # A thin wrapper for people who want to simplify their code and make it easier to read
    return yesno(title,contents,theme=theme,values=values,add_cancel=True)

def okay(title,contents,theme='System',value='OK'):   
    root = ctk.CTk()
    root.title(title)
    root.overrideredirect(True) # Disable the window bar

    screen_width = root.winfo_screenwidth() # Get width/height to center the window
    screen_height = root.winfo_screenheight()
    root.geometry(f'250x120+{(screen_width//2)-125}+{(screen_height//2)-60}')
    
    ctk.set_appearance_mode(theme)
    
    title_ui = ctk.CTkLabel(root,text=title,font=('Arial',16))
    title_ui.pack(pady=10)
    
    contents_ui = ctk.CTkLabel(root,text=contents,font=('Arial',12))
    contents_ui.pack()
    
    def terminate_window(root): # Yes, I know a function inside a function is not recommended, but it works
        root.quit()
        root.destroy()
    
    values_ui = ctk.CTkSegmentedButton(root,values=[value],height=25,command=lambda _: terminate_window(root)) # likely a better way to do that, but it works
    values_ui.pack(pady=10)
    
    root.mainloop()

def textinput(title,contents,theme='System',oldtext=''):
    global _rv
    _rv = None
    
    root = ctk.CTk()
    root.title(title)
    try:
        root.attributes('-type','dock') # the Entry is not highlighting, this works on linux only
    except:
        pass

    screen_width = root.winfo_screenwidth() # Get width/height to center the window
    screen_height = root.winfo_screenheight()
    root.geometry(f'250x160+{(screen_width//2)-125}+{(screen_height//2)-80}')
    
    ctk.set_appearance_mode(theme)
    
    title_ui = ctk.CTkLabel(root,text=title,font=('Arial',16))
    title_ui.pack(pady=10)
    
    contents_ui = ctk.CTkLabel(root,text=contents,font=('Arial',12))
    contents_ui.pack()
    
    def return_val(root): # Yes, I know a function inside a function is not recommended, but it works
        global _rv
        _rv = entry_ui.get()
        root.quit()
        root.destroy()
    
    entry_ui = ctk.CTkEntry(root,placeholder_text=oldtext,font=('Arial',12))
    entry_ui.pack(pady=10)
    
    ok_ui = ctk.CTkSegmentedButton(root,values=['Submit'],height=25,command=lambda _: return_val(root)) # I know I could use ctkbutton, but I want a uniform gui
    ok_ui.pack()
    
    entry_ui.bind('<Button-1>', lambda event: entry_ui.focus_force())
    
    root.mainloop()
    
    return _rv # This is the only way to return the value, as putting return in return_val would just close the dialogue and not return anything