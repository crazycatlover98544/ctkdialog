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

This is a demonstration of ctkdialog. This program expects "ctkdialog.py" in the same directory as it. You can also (not supported by me) add ctkdialog as a module.
'''

import ctkdialog

yn = ctkdialog.yesno('Should I Come','Should I come into this game?')
ync = ctkdialog.yesnocancel('Save','Do you want to save this important work?') # This is a wrapper of ctkdialog.yesno(title,content,add_cancel=True)
o = ctkdialog.okay('Alert','The danger is here!')
ti = ctkdialog.textinput('Enter Code','Enter the 4-digit code from the game card.')

print('Answers:')
print(f'yesno dialog:        {yn}')
print(f'yesnocancel dialog:  {ync}')
print(f'okay dialog:         {o}')
print(f'textinput dialog:    {ti}')