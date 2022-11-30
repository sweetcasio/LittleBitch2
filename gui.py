from tkinter import *
from tkinter import ttk
from tkinter import messagebox 
import play
import time
import record
import threading
import file
import keyboard

BG = '#e381ce'
BUTTON_BG = '#d8c2ff'
LIST_BG = '#d8dd2f'
FG = '#FFFFFF'
RESOLUTION = '400x200'
STAR_ICO = 'star.ico'
FONT = ('Consolas', 16)




def button(text=None, command=None):
    return Button(text=text, font=FONT, bg=BUTTON_BG, fg=FG, command=command, relief=FLAT)

def run():

    def on_close():
        if any([t.getName() in ['record', 'play'] for t in threading.enumerate()]):
            cat = cat_text['text']
            cat_text['text'] = '*^o_O^*'
            messagebox.askokcancel('Нельзя так делать!', 'Прекратите запись или проигрывание!\n*^⨯w⨯^*')
            cat_text['text'] = cat
        else:
            try:
                window.destroy()
            except:
                window.destroy()


    def digit_limit(a, b, c):
        if not filebox.get().strip().isdigit():
            filebox.set(' 1')

    def character_limit(a, b, c):
        if len(filebox.get()) > 2:
            filebox.set(filebox.get()[:2])

    def on_file_change(a, b, c):
        try:
            i = int(filebox.get()) - 1
            file.current = file.files[i]
        except:
            ...

    recording = False
    def on_record_click():
        file_list['state'] = 'disabled'
        play_button['state'] = 'disabled'
        nonlocal recording
        if recording:
            return
        recording = True
        cat_text['text'] = '*^oωo^*'
        def record_thread():
            nonlocal recording
            record.record()
            head_text['text'] = 'Остановлено [' + filebox.get().strip() + ']!'
            cat_text['text'] = '*^-ω-^*'
            recording = False
            file_list['state'] = 'normal'
            play_button['state'] = 'normal'
            

        thread = threading.Thread(target=record_thread, name='record')
        thread.start()
        head_text['text'] = 'Запись [' + filebox.get().strip() + ']...'


    playing = False
    def on_play_click():
        file_list['state'] = 'disabled'
        record_button['state'] = 'disabled'
        nonlocal playing
        if playing:
            return 
        
        playing = True
        cat_text['text'] = '*^oωo^*'
        def play_thread():
            nonlocal playing
            play.play()
            head_text['text'] = 'Остановлено [' + filebox.get().strip() + ']!'
            cat_text['text'] = '*^-ω-^*'
            playing = False
            file_list['state'] = 'normal'
            record_button['state'] = 'normal'
        
        def stop(event):
            nonlocal cnt
            cnt = False

        keyboard.hook_key('esc', stop)
        cnt = True
        def countdown():
            nonlocal cnt
            for i in range(5, 0, -1):
                head_text['text'] = str(i)
                head_text.update()
                time.sleep(1)
                if not cnt:
                    return False
            return True


        if countdown():
            thread = threading.Thread(target=play_thread, name='play')
            thread.start()

            head_text['text'] = 'Воспроизведение [' + filebox.get().strip() + ']...'
        else:
            cat_text['text'] = '*^>ω<^*'
            head_text['text'] = 'Прервано!'
            file_list['state'] = 'normal'
            record_button['state'] = 'normal'
            playing = False
        keyboard.unhook_all()
        
        

    window = Tk()
    window['bg'] = BG
    window.geometry(RESOLUTION)
    window.resizable(0, 0)
    window.iconbitmap('star.ico')
    window.title('FullGround *^.ω.^*')
    window.protocol('WM_DELETE_WINDOW', on_close)
    

    filebox = StringVar(value=' 1')
    filebox.trace_add('write', digit_limit)
    filebox.trace_add('write', on_file_change)
    filebox.trace_add('write', character_limit)

    head_text = Label(window, text='', font=FONT, fg=FG, bg=BG)
    record_button = button('Запись', on_record_click)
    play_button = button('Играть', on_play_click)
    file_list = ttk.Combobox(window, values=(' 1', ' 2', ' 3', ' 4'), font=('Consolas', 12), textvariable=filebox)
    info_text = Label(window, text='[esc] -> остановить', bg=BG, font=('Consolas', 8), fg=FG)

    cat_text = Label(window, text='*^-ω-^*', font=FONT, bg=BG, fg=FG)

    head_text.place(relx=.5, rely=.2, anchor=CENTER)
    record_button.place(relx=.3, rely=.5, anchor=CENTER)
    play_button.place(relx=.7, rely=.5, anchor=CENTER)
    file_list.place(relx=.5, rely=.5, anchor=CENTER, relwidth=.1)
    info_text.place(relx=.5, rely=.94, anchor=CENTER)
    cat_text.place(relx=.5, rely=.75, anchor=CENTER)

    window.mainloop()

