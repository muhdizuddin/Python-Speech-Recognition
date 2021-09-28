#must install = pip install malaya-speech
import speech_recognition as sr
import malaya_speech
malayspeech, sr = malaya_speech.load('Your voice directory (file must in wav format)')
malayspeech
small_model = malaya_speech.stt.deep_transducer(model = 'small-conformer')
small_model.greedy_decoder([malayspeech])
model = malaya_speech.stt.deep_transducer(model = 'conformer')
model.greedy_decoder([malayspeech])
