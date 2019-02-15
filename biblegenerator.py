# -*- coding: utf-8 -*-
import random

class Bible:
    
    passages = {'Mark 6:4' : 'Jesus said to them, "A prophet is not without honor except in his own town, among his relatives and in his own home."', 
    'John 3:16' : 'For God so loved the world that he gave his one and only Son, that whoever believes in him shall not perish but have eternal life.',
        'James 1:2' : 'Consider it pure joy, my brothers and sisters, whenever you face trials of many kinds',
        'Romans 12:21' : 'Do not be overcome by evil, but overcome evil with good.',
        'Isaiah 54:17' : '"No weapon that is formed against you will prosper; and every tongue that accuses you in judgment you will condemn. This is the heritage of the servants of the Lord, and their vindication is from Me," declares the Lord."',
        'John 10:10' : '"The thief comes only to steal and kill and destroy. I came that they may have life and have it abundantly."',
        'Isaiah 43:19' : 'See, I am doing a new thing! Now it springs up; do you not perceive it? I am making a way in the wilderness and streams in the wasteland.',
        '2 Timothy 1:7' : 'For God hath not given us the spirit of fear; but of power, and of love, and of a sound mind.',
        '2 Chronicles 20:15' : '''"This is what the LORD says to you: 'Do not be afraid or discouraged because of this vast army. For the battle is not yours, but God's"''',
                'Mark 10:9' : '''Therefore what God has joined together, let no one separate.”'''
    }
    
    def __init__(self):
        pass
    
    def rpass(self):
        self.script, self.passage = random.choice(list(self.passages.items()))
        return self.script, self.passage
    
a = Bible()

script, passage = a.rpass()

print(script)
print(passage)

    
