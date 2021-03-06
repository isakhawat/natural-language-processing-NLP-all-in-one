# -*- coding: utf-8 -*-
"""speech to voice.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1xhVqTqPQd6O2PpEG-O_VKDxFITD-Ey3g
"""

# Import the required module for text 
# to speech conversion
from gtts import gTTS
from playsound import playsound
 
# This module is imported so that we can 
# play the converted audio
import os
 
# The text that you want to convert to audio
mytext = 'My Baby samraddhi is playing with my mobile phone.Amazing my dear!'
 
# Language in which you want to convert
language = 'en'
 
# Passing the text and language to the engine, 
# here we have marked slow=False. Which tells 
# the module that the converted audio should 
# have a high speed
myobj = gTTS(text=mytext, lang=language, slow=False)
 
# Saving the converted audio in a mp3 file named
# welcome 
myobj.save("welcome.mp3")
 
# Playing the converted file
#os.system("mpg321 welcome.mp3")
playsound("welcome.mp3")

!pip install gTTS

# Import the required module for text  
# to speech conversion 
from gtts import gTTS 
  
# This module is imported so that we can  
# play the converted audio 
import os 
  
# The text that you want to convert to audio 
mytext = 'দুর্নীতি দমন কমিশনের (দুদক) মামলায় সাবেক প্রধান বিচারপতি এস কে সিনহাসহ ১১ জন পলাতক আসামির নামে জাতীয় পত্রিকায় বিজ্ঞপ্তি প্রকাশের নির্দেশ দিয়েছেন আদালত। ঢাকা মহানগরের সিনিয়র স্পেশাল জজ কে এম ইমরুল কায়েস আজ বুধবার এ আদেশ দেন।আদালত সূত্র বলছে, এর আগে ৫ জানুয়ারি সাবেক প্রধান বিচারপতি এস কে সিনহাসহ ১১ জনের বিরুদ্ধে গ্রেপ্তারি পরোয়ানা জারি করেন আদালত। আজ ওই গ্রেপ্তারি পরোয়ানার তামিল প্রতিবেদন জমা দেওয়ার দিন ধার্য ছিল। পুলিশের পক্ষ থেকে আদালতে প্রতিবেদন দিয়ে বলা হয়, এস কে সিনহাসহ অন্যদের গ্রেপ্তার করা যায়নি। আদালত ওই প্রতিবেদন দিয়ে তাঁদের বিরুদ্ধে পত্রিকায় বিজ্ঞপ্তি প্রকাশের নির্দেশ দেন। এ–সংক্রান্ত প্রতিবেদন ও মামলার শুনানির জন্য নতুন দিন ঠিক করা হয়েছে আগামী ২০ ফেব্রুয়ারি।'
# Language in which you want to convert 
language = 'bn'
  
# Passing the text and language to the engine,  
# here we have marked slow=False. Which tells  
# the module that the converted audio should  
# have a high speed 
myobj = gTTS(text=mytext, lang=language, slow=False) 
  
# Saving the converted audio in a mp3 file named 
# welcome  
myobj.save("welcome.mp3") 
  
# Playing the converted file 
os.system("mpg321 welcome.mp3")

!pip install playsound

from gtts import gTTS
import playsound
import os
tts = gTTS(text='দর্শকেরা আমি তানভীর ইসলাম ইস্ত্রিম । চাইতেছি বাংলা  সহকারি বানাতে ? আর সেটা উন্মুক্ত করে দিতে । আপনারা কি এই প্রোজেক্ট এ কাজ করবেন ? ', lang='bn')
tts.save("good.mp3")
os.system("mpg321 good.mp3")
playsound.playsound('good.mp3', True)