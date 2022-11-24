# compiler-GUI-using-tkinter
GUI that allows user to choose a java file and check whether the nesting have been done correctly
group members
Noo maxwell owiti..........com/b/01-01819/2020
Brian otieno...............com/b/01-00099/2018
Hillary Kipkoech............com/b/01-00173/2020

## Tkinter documentation

The tkinter package (“Tk interface”) is the standard Python interface to the Tcl/Tk GUI toolkit. Both Tk and tkinter are available on most Unix platforms, including macOS, as well as on Windows systems.

Running python -m tkinter from the command line should open a window demonstrating a simple Tk interface, letting you know that tkinter is properly installed on your system, and also showing what version of Tcl/Tk is installed, so you can read the Tcl/Tk documentation specific to that version.

Tkinter supports a range of Tcl/Tk versions, built either with or without thread support. The official Python binary release bundles Tcl/Tk 8.6 threaded. See the source code for the _tkinter module for more information about supported versions.

Tkinter is not a thin wrapper, but adds a fair amount of its own logic to make the experience more pythonic. This documentation will concentrate on these additions and changes, and refer to the official Tcl/Tk documentation for details that are unchanged.

### Architecture

Tcl/Tk is not a single library but rather consists of a few distinct modules, each with separate functionality and its own official documentation. Python’s binary releases also ship an add-on module together with it.

Tcl
Tcl is a dynamic interpreted programming language, just like Python. Though it can be used on its own as a general-purpose programming language, it is most commonly embedded into C applications as a scripting engine or an interface to the Tk toolkit. The Tcl library has a C interface to create and manage one or more instances of a Tcl interpreter, run Tcl commands and scripts in those instances, and add custom commands implemented in either Tcl or C. Each interpreter has an event queue, and there are facilities to send events to it and process them. Unlike Python, Tcl’s execution model is designed around cooperative multitasking, and Tkinter bridges this difference (see Threading model for details).

Tk
Tk is a Tcl package implemented in C that adds custom commands to create and manipulate GUI widgets. Each Tk object embeds its own Tcl interpreter instance with Tk loaded into it. Tk’s widgets are very customizable, though at the cost of a dated appearance. Tk uses Tcl’s event queue to generate and process GUI events.

Ttk
Themed Tk (Ttk) is a newer family of Tk widgets that provide a much better appearance on different platforms than many of the classic Tk widgets. Ttk is distributed as part of Tk, starting with Tk version 8.5. Python bindings are provided in a separate module, tkinter.ttk.

Internally, Tk and Ttk use facilities of the underlying operating system, i.e., Xlib on Unix/X11, Cocoa on macOS, GDI on Windows.

When your Python application uses a class in Tkinter, e.g., to create a widget, the tkinter module first assembles a Tcl/Tk command string. It passes that Tcl command string to an internal _tkinter binary module, which then calls the Tcl interpreter to evaluate it. The Tcl interpreter will then call into the Tk and/or Ttk packages, which will in turn make calls to Xlib, Cocoa, or GDI.

#### Tkinter Modules

Support for Tkinter is spread across several modules. Most applications will need the main tkinter module, as well as the tkinter.ttk module, which provides the modern themed widget set and API:

from tkinter import *
from tkinter import ttk

##### widgets that can be created using tkinter
These are 19 widgets available in Python Tkinter module. Below we have all the widgets listed down with a basic description:

Button	-If you want to add a button in your application then Button widget will be used.
Canvas	-To draw a complex layout and pictures (like graphics, text, etc.)Canvas Widget will be used.
CheckButton -	If you want to display a number of options as checkboxes then Checkbutton widget is used. It allows you to select multiple options at a time.
Entry	-To display a single-line text field that accepts values from the user Entry widget will be used.
Frame -	In order to group and organize another widgets Frame widget will be used. Basically it acts as a container that holds other widgets.
Label -	To Provide a single line caption to another widget Label widget will be used. It can contain images too.
Listbox - To provide a user with a list of options the Listbox widget will be used.
Menu -	To provides commands to the user Menu widget will be used. Basically these commands are inside the Menubutton. This widget mainly creates all kinds of Menus required in the application.
Menubutton -	The Menubutton widget is used to display the menu items to the user.
Message -	The message widget mainly displays a message box to the user. Basically it is a multi-line text which is non-editable.
Radiobutton -	If you want the number of options to be displayed as radio buttons then the Radiobutton widget will be used. You can select one at a time.
Scale -	Scale widget is mainly a graphical slider that allows you to select values from the scale.
Scrollbar -	To scroll the window up and down the scrollbar widget in python will be used.
Text -	The text widget mainly provides a multi-line text field to the user where users and enter or edit the text and it is different from Entry.
Toplevel - The Toplevel widget is mainly used to provide us with a separate window container
SpinBox -	The SpinBox acts as an entry to the "Entry widget" in which value can be input just by selecting a fixed value of numbers.
PanedWindow -	The PanedWindow is also a container widget that is mainly used to handle different panes. Panes arranged inside it can either Horizontal or vertical
##### summary
generally the Tkinter llibrary is a good deal,one can create a gui without alot of concerns of importing other modules.since  tkinter is an inbuilt module and is generally simple to use.
LabelFrame -	The LabelFrame widget is also a container widget used to mainly handle the complex widgets.
MessageBox -	The MessageBox widget is mainly used to display messages in the Desktop applications.
