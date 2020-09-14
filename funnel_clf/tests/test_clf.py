from funnel_clf.core import get_body
import email
import pkg_resources

test_email = """
'From: suraj@apollo.cs.jhu.edu (Suraj Surendrakumar)\nSubject: ==> NEW STEREO SYSTEM/COMPONENTS FOR SALE <==\nOrganization: 
The Johns Hopkins University CS Department\nDistribution: usa\nLines: 29\n\n\n\n10 month old stereo system for sale.
 Luxman R-351 receiver, Onkyo TA-RW404\ntape deck, and Polk Monitor M4.6 book shelf speakers are for sale. Receiver\nhas 5 year warranty,
  and all equipment is in excellent condition. Paid $950\nfor the system and willing to consider the best offer. Will sell seperate\npieces also 
  if desired. Please send best offer to suraj@cs.jhu.edu.\n\nSpeakers: Polk Monitor M4.6 bookshelf speakers\n\t  Paid $250 pair. Willing to consider
   best offer.\n\nReceiver: Luxman R-351 receiver with 5 year (yes 5 years) warranty.\n\t  Paid $475. Willing to consider best offer.\n\t  
   Full remote, 2 pairs of speaker connections,\n\t  60 watts per channel, but drives like a 150 watts per channel\n\t  
   Has all the standard features, and more.\n\nTape Deck: Onkyo TA-RW404 tape deck\n\t   Paid $275. Willing to consider best offer.\n\t  
    Dual cassette, Dolby B, C, and HX Pro.\n\t   Input level control for recording, auto reverse both sides.\n          
     Has all standard features.\n\nSend E-mail with best offer to suraj@cs.jhu.edu\n\n-Suraj\n\n\n\n'"""


def test_get_body():
    parser = email.parser.Parser()
    msg = parser.parsestr(test_email)
    body = get_body((msg))
    assert body is not None
