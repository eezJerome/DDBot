# DDBot
Discord Drake Bot - an attempt at using RNNs and LSTMs for rapping bots

link to h5 file with saved model and weights trained on like 50 songs of ab-soul
https://drive.google.com/file/d/1oatNL-LCre0cK2M73nYp8TT-h5xF95EI/view?usp=sharing

link to h5 file with saved model and weights trained on like 50 songs of drake
https://drive.google.com/file/d/1Ox9P2bGjj1MODJGqzuQNeeQIG4hqkiVu/view?usp=sharing

**i ripped the code from NLP: Zero to Hero tutorial by Tensorflow because i'm a terrible human being.
all credits go to their rightful owners
link to original colab: https://colab.research.google.com/github/lmoroney/dlaicourse/blob/master/TensorFlow%20In%20Practice/Course%203%20-%20NLP/Course%203%20-%20Week%204%20-%20Lesson%202%20-%20Notebook.ipynb#scrollTo=6Vc6PHgxa6Hm
**
using python with tensorflow.keras to create model, trained on 75 epochs to about 87% accuracy; model stopped training at random intervals, so 75 was the sweet spot. However, feel free to experiment with your epochs.

**In the event that the lyrics are not writing to your file, simply open lyrics file in notepad, save as another file, and change encoding to ANSI. This fixed any issues when the model could not read the text file**

not sure how to wrap this or whatever to discord; probably use JS which is zeke's forte
