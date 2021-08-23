
#-----Statement of Authorship----------------------------------------#
#
#  This is an individual assessment item.  By submitting this
#  code I agree that it represents my own work.  I am aware of
#  the University rule that a student must not act in a manner
#  which constitutes academic dishonesty as stated and explained
#  in QUT's Manual of Policies and Procedures, Section C/5.3
#  "Academic Integrity" and Section E/2.1 "Student Code of Conduct".
#
#    Student no: n10261371
#    Student name: Anson Tam
#
#  NB: Files submitted without a completed copy of this statement
#  will not be marked.  Submitted files will be subjected to
#  software plagiarism analysis using the MoSS system
#  (http://theory.stanford.edu/~aiken/moss/).
#
#--------------------------------------------------------------------#



#-----Assignment Description-----------------------------------------#
#
#  Online Shopping Application
#
#  In this assignment you will combine your knowledge of HTMl/XML
#  mark-up languages with your skills in Python scripting, pattern
#  matching, and Graphical User Interface design to produce a useful
#  application for simulating an online shopping experience.  See
#  the instruction sheet accompanying this file for full details.
#
#--------------------------------------------------------------------#



#-----Imported Functions---------------------------------------------#
#
# Below are various import statements for helpful functions.  You
# should be able to complete this assignment using these
# functions only.  Note that not all of these functions are
# needed to successfully complete this assignment.
#

# The function for opening a web document given its URL.
# (You WILL need to use this function in your solution
# either directly or via our "download" function.)
from urllib.request import urlopen

# Import the standard Tkinter functions. (You WILL need to use
# these functions in your solution.)
from tkinter import *

# Functions for finding all occurrences of a pattern
# defined via a regular expression, as well as
# the "multiline" and "dotall" flags.  (You do NOT need to
# use these functions in your solution, because the problem
# can be solved with the string "find" function, but it will
# be difficult to produce a concise and robust solution
# without using regular expressions.)
from re import findall, finditer, MULTILINE, DOTALL

# Import the standard SQLite functions (just in case they're
# needed).
from sqlite3 import *

#
#--------------------------------------------------------------------#



#-----Downloader Function--------------------------------------------#
#
# This is our function for downloading a web page's content and both
# saving it on a local file and returning its source code
# as a Unicode string. The function tries to produce
# a meaningful error message if the attempt fails.  WARNING: This
# function will silently overwrite the target file if it
# already exists!  NB: You should change the filename extension to
# "xhtml" when downloading an XML document.  (You do NOT need to use
# this function in your solution if you choose to call "urlopen"
# directly, but it is provided for your convenience.)
#
def download(url = 'http://www.wikipedia.org/',
             target_filename = 'download',
             filename_extension = 'html'):

    # Import an exception raised when a web server denies access
    # to a document
    from urllib.error import HTTPError

    # Open the web document for reading
    try:
        web_page = urlopen(url)
    except ValueError:
        raise Exception("Download error - Cannot find document at URL '" + url + "'")
    except HTTPError:
        raise Exception("Download error - Access denied to document at URL '" + url + "'")
    except:
        raise Exception("Download error - Something went wrong when trying to download " + \
                        "the document at URL '" + url + "'")

    # Read its contents as a Unicode string
    try:
        web_page_contents = web_page.read().decode('UTF-8')
    except UnicodeDecodeError:
        raise Exception("Download error - Unable to decode document at URL '" + \
                        url + "' as Unicode text")

    # Write the contents to a local text file as Unicode
    # characters (overwriting the file if it
    # already exists!)
    try:
        text_file = open(target_filename + '.' + filename_extension,
                         'w', encoding = 'UTF-8')
        text_file.write(web_page_contents)
        text_file.close()
    except:
        raise Exception("Download error - Unable to write to file '" + \
                        target_file + "'")

    # Return the downloaded document to the caller
    return web_page_contents

#
#--------------------------------------------------------------------#



#-----Student's Solution---------------------------------------------#
#
# Put your solution at the end of this file.
#

# Name of the invoice file. To simplify marking, your program should
# generate its invoice using this file name.
invoice_file = 'invoice.html'
from bs4 import BeautifulSoup

watch  = []
tshirts = []
cart = []
hats = []
global radiobtnClicked
global spinBox
#Code For UI
import tkinter as tk

def productList(event):
    global radiobtnClicked
    


    if event == 1:
       radiobtnClicked =1 
       title = "Hats"
       page = download(url = 'http://www.westernhatstore.com/childrens-western-hats/',target_filename = 'hats',filename_extension = 'html')
       page_html = BeautifulSoup(page ,"html.parser" )
       page_content = page_html.find("ul",{"class":"ProductList"})
       page_contents = page_content.find_all("li")


       for page_content in page_contents:
            dataDict = dict()
            dataDict['Name'] = page_content.div.nextSibling.nextSibling.a.string
            dataDict['Image_Url'] = page_content.div.a.img['src']

            price_text = page_content.em.string
            price = price_text[1:]
            dataDict['Price'] = price
            hats.append(dataDict)
    

       #print(hats)
        
       #Creating New Window
       newWindow = tk.Tk()
       newWindow.geometry('400x550')

       #Title
       newWindow.title(title)

       #Heading
       lblNewWindowHeader = tk.Label(newWindow, text=title, bg="green" )
       lblNewWindowHeader.grid(row = 0 ,column = 0 , columnspan = 3)
       lblNewWindowHeader.config(font=('times',12, 'bold'))
       lblNewWindowHeader.config(justify=tk.CENTER,width =44)
        
       #Content
       textContent = tk.Text(newWindow, height=31, width=49,relief="ridge",borderwidth=2 , bg="green")
        
       textContent.grid(row = 1 ,column = 0, rowspan = 3)
        
       #URL
       lblURL = tk.Label(newWindow, text="URL", bg="green" )
       lblURL.grid(row = 11,column = 0 , columnspan = 3)
       lblURL.config(justify=tk.CENTER,width =57)
       lblURL.config(text="http://www.westernhatstore.com/childrens-western-hats/")

       #Populating Product
       #print(hats[3]['Name'])
       textContent.config(state = 'normal')
       i = 0
       for i in range(10):
          textContent.insert(tk.END,'#')
          textContent.insert(tk.END,i+1)
          textContent.insert(tk.END,': ')
          
          textContent.insert(tk.END,hats[i]['Name'])
          textContent.insert(tk.END,'(')
          textContent.insert(tk.END,hats[i]['Price'])
          textContent.insert(tk.END,')')
          textContent.insert(tk.END,'\n')
          
          #i = i + 1
       textContent.config(state = 'disabled')
    elif event== 2:
       radiobtnClicked =2
       title = "Watch"
       
       page = download(url = 'https://www.one-prices.com/',target_filename = 'watch',filename_extension = 'html')
       page_html = BeautifulSoup(page ,"html.parser" )
       page_contents = page_html.findAll("li",{"class":"index_pic"})

       for page_content in page_contents:
            dataDict = dict()
            dataDict['Name'] = page_content.nextSibling.a.string
            img_url = page_content.a.img['src']
            image_url = "https://www.one-prices.com/"+img_url
            dataDict['Image_Url'] = image_url

            price_text = page_content.nextSibling.nextSibling.string
            price = price_text.split(" ")
            dataDict['Price'] = price[2]
            watch.append(dataDict)
    

       
        
       #Creating New Window
       newWindow = tk.Tk()
       newWindow.geometry('400x550')

       #Title
       newWindow.title(title)

       #Heading
       lblNewWindowHeader = tk.Label(newWindow, text=title, bg="green" )
       lblNewWindowHeader.grid(row = 0 ,column = 0 , columnspan = 3)
       lblNewWindowHeader.config(font=('times',12, 'bold'))
       lblNewWindowHeader.config(justify=tk.CENTER,width =44)
        
       #Content
       textContent = tk.Text(newWindow, height=31, width=49,relief="ridge",borderwidth=2 , bg="green")
        
       textContent.grid(row = 1 ,column = 0, rowspan = 3)
        
       #URL
       lblURL = tk.Label(newWindow, text="URL", bg="green" )
       lblURL.grid(row = 11,column = 0 , columnspan = 3)
       lblURL.config(justify=tk.CENTER,width =57)
       lblURL.config(text="https://www.one-prices.com/")
       textContent.config(state = 'normal')
       i = 0
       for i in range(10):
          textContent.insert(tk.END,'#')
          textContent.insert(tk.END,i+1)
          textContent.insert(tk.END,': ')
          textContent.insert(tk.END,watch[i]['Name'])
          textContent.insert(tk.END,'(')
          textContent.insert(tk.END,watch[i]['Price'])
          textContent.insert(tk.END,')')
          textContent.insert(tk.END,'\n')
         
          #i = i + 1
       textContent.config(state = 'disabled')
    elif event == 3:

       radiobtnClicked =3
       title = "T-Shirts"
       
       
       page = download(url = 'https://www.thinkgeek.com/clothing/t-shirts/',target_filename = 'tshirts',filename_extension = 'html')
       page_html = BeautifulSoup(page ,"html.parser" )
       page_contents = page_html.findAll("div",{"class":"product"})

       for page_content in page_contents:
            dataDict = dict()
            dataDict['Name'] = page_content.a.h4.string
            img_url = page_content.a.img['src']
            image_url = "https://www.thinkgeek.com"+img_url
            dataDict['Image_Url'] = image_url

            price_text = page_content.p.contents[0].strip()
            price = price_text[1:]
            dataDict['Price'] = price
            tshirts.append(dataDict)
       
    

       
        
       #Creating New Window
       newWindow = tk.Tk()
       newWindow.geometry('400x550')

       #Title
       newWindow.title(title)

       #Heading
       lblNewWindowHeader = tk.Label(newWindow, text=title, bg="green" )
       lblNewWindowHeader.grid(row = 0 ,column = 0 , columnspan = 3)
       lblNewWindowHeader.config(font=('times',12, 'bold'))
       lblNewWindowHeader.config(justify=tk.CENTER,width =44)
        
       #Content
       textContent = tk.Text(newWindow, height=31, width=49,relief="ridge",borderwidth=2 , bg="green")
        
       textContent.grid(row = 1 ,column = 0, rowspan = 3)
        
       #URL
       lblURL = tk.Label(newWindow, text="URL", bg="green" )
       lblURL.grid(row = 11,column = 0 , columnspan = 3)
       lblURL.config(justify=tk.CENTER,width =57)
       lblURL.config(text="https://www.thinkgeek.com/clothing/t-shirts/")
       textContent.config(state = 'normal')
       i = 0
       for i in range(10):
          textContent.insert(tk.END,'#')
          textContent.insert(tk.END,i+1)
          textContent.insert(tk.END,': ')
          textContent.insert(tk.END,tshirts[i]['Name'])
          textContent.insert(tk.END,'(')
          textContent.insert(tk.END,tshirts[i]['Price'])
          textContent.insert(tk.END,')')
          textContent.insert(tk.END,'\n')
          
          #i = i + 1
       textContent.config(state = 'disabled')
    elif  event== 4:
       radiobtnClicked =4
       print ("hello")

   
    newWindow.mainloop()



      
#main Function
def main():
      global spinBox
      # Creating the window
      root = tk.Tk()
      root.geometry('500x320')

      var = tk.IntVar()
      #Title
      root.title('Abay shopping App')
      root.configure(background="#b20833")

      #Header Text
      lblHeader = tk.Label(root, text='The Power of All of Us' , bg="#b20833")
      lblHeader.grid(row=0, column=0,columnspan =4)
      lblHeader.config(font=('times',15, 'bold'))
      lblHeader.config(justify=tk.CENTER,width=44)
      
      #Logo
      canvasLogo = Canvas(root, width = 300, height = 280,bg="#b20833")
      canvasLogo.grid(row=1, column=0,rowspan=4, columnspan= 2)
      
      #Logo Image
      logo = PhotoImage(file="logo.png")      
      canvasLogo.create_image(10,10, anchor=NW, image=logo)


      #Radio Button Group One
      lblframeOne = LabelFrame(root, text="Bargain Bin   ",bg="#b20833")
      lblframeOne.grid(row=1, column=2,columnspan= 2)

      radioBtnOne = Radiobutton(lblframeOne, text="Hats     ",variable=var,  value=1 ,command=lambda *args: productList(1),bg="#b20833")
      radioBtnOne.grid(row=0, column=0)

      radioBtnTwo = Radiobutton(lblframeOne, text="Watch     ", variable=var,  value=2 ,command=lambda *args: productList(2),bg="#b20833")
      radioBtnTwo.grid(row=0, column=1)
   
      
      #Radio Button Group Two
      lblframeTwo = LabelFrame(root, text="Today's Special",bg="#b20833")
      lblframeTwo.grid(row=2, column=2,columnspan= 2)

      radioBtnThree = Radiobutton(lblframeTwo, text="T-Shirts", variable=var,  value=3,command=lambda *args: productList(3),bg="#b20833")
      radioBtnThree.grid(row=0, column=0)

      radioBtnFour = Radiobutton(lblframeTwo, text="Option 4", variable=var,  value=4 ,command=lambda *args: productList(4),bg="#b20833")
      radioBtnFour.grid(row=0, column=1)
      

      #Label for 
      lblItemNumberlbl = tk.Label(root, text="Item Number",bg="#b20833")
      lblItemNumberlbl.grid(row=3, column=2)
      
      #Spinbox
      spinBox = Spinbox(root, from_=0, to=10,bg="#b20833")
      #lblItemNumber = tk.Label(root, text="###")
      spinBox.grid(row=3, column=3)

      #Add to Cart Button
      btnAddToCart = tk.Button(root, text="Add To Cart" , command=addToCart)
      btnAddToCart.grid(row=4, column=2)

      #Print Invoice Button
      btnPrintInvoice = tk.Button(root, text="Print Invoice" ,command=printInvoice)
      btnPrintInvoice.grid(row=4, column=3)
    #   lblLoanAmount = tk.Label(root, text="Loan Amount").grid(row=3, column=0)
    #   lblMonthlyPay = tk.Label(root, text="Monthly Payment").grid(row=4, column=0)
    #   lblTotalPay = tk.Label(root, text="Total Payment").grid(row=5, column=0)
      
      #pack(fill="both", expand="yes")
 
    #   left = Label(lblframeOne, text="Inside the LabelFrame")
    #   left.pack()
     
      root.mainloop()

def addToCart():
    
    if radiobtnClicked == 1:
       dataDict = dict()
       choice = int(spinBox.get())
       dataDict['Name'] = hats[choice]['Name']
       dataDict['Image_Url']= hats[choice]['Image_Url']
       dataDict['Price'] = hats[choice]['Price']
       cart.append(dataDict)
        

    elif  radiobtnClicked == 2:
       dataDict = dict()
       choice = int(spinBox.get())
       dataDict['Name'] = hats[choice]['Name']
       dataDict['Image_Url']= hats[choice]['Image_Url']
       dataDict['Price'] = hats[choice]['Price']
       cart.append(dataDict)
    elif  radiobtnClicked == 3:
       dataDict = dict()
       choice = int(spinBox.get())
       dataDict['Name'] = hats[choice]['Name']
       dataDict['Image_Url']= hats[choice]['Image_Url']
       dataDict['Price'] = hats[choice]['Price']
       cart.append(dataDict)

    elif  radiobtnClicked == 4:
       print (radiobtnClicked)
def printInvoice():
    total_bill=0
    invoice_products = ""
    for x in cart:
        total_bill = total_bill + float(x['Price'])
    invoice_header ="<!DOCTYPE html><html><head><title>Abay shopping App Invoice</title></head><body>"
    invoice_heading ="<center><b><h1>Abay shopping App Invoice</h1</b>>"
    invoide_logo = "<img src='logo.png'>"
    invoice_subheading = "<b><h2>Total for the purchases below :"+str(total_bill)+"</h2>AUD<p>(Prompt payment is appreciated!)</p</b>"
    

    for x in cart:
        invoice_products = invoice_products + "<b><h2>"+ x['Name']+"</h2></b><img src='"+x['Image_Url'] +"'><p>Our Price: $"+x['Price'] +"USD</p>"
        
    
    invoice_footer= "</center></body></html>"
    invoice = invoice_header + invoice_heading+ invoide_logo +invoice_subheading + invoice_products +invoice_footer

    f = open(invoice_file,'w')
    f.write(invoice)
    f.close()


#Calling the main function  

if __name__== "__main__":
  main()
