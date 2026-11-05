"""
===========================================================
Topic: Theme extraction for synthetic reading
===========================================================
Author Name(s): [Enter Student Name(s)]
Short Description: Themes extracted by a local LLM (qwen2.5-7b-instruct, LM Studio)
from corpus/sultanas_dream.txt, read in 4 ordered segments. Research question:
How does Sultana's Dream reverse the gendered division of space, work and knowledge, and what does that reversal say about the purdah system it is criticising?
quote_verified is True when the quotation was found word for word in the
segment; check every False entry by hand before using it.
Semester: Monsoon Semester 2026
Affiliation: [Enter Department and Institution Name]
===========================================================
"""

research_question = "How does Sultana's Dream reverse the gendered division of space, work and knowledge, and what does that reversal say about the purdah system it is criticising?"

theme_vocabulary = ['Spatial segregation (zenana and mardana)',
 'Reversal of gender roles',
 "Women's education and science",
 'Critique of male governance and war',
 'Domestic labour and the household',
 'Technology and nature',
 'Colonial and social context',
 "Narrator's doubt and the dream frame"]

theme_data = [{'segment': 1,
  'theme': 'Spatial segregation (zenana and mardana)',
  'evidence': 'We shut our men indoors.',
  'note': 'This passage indicates that the women are kept in a separate area, which is '
          'consistent with the purdah system.',
  'strength': 2,
  'quote_verified': True},
 {'segment': 1,
  'theme': 'Reversal of gender roles',
  'evidence': 'You need not be afraid of coming across a man here. This is Ladyland, '
              'free from sin and harm. Virtue herself reigns here.',
  'note': 'This passage shows the reversal of traditional gender roles by presenting '
          'women as virtuous in an environment where men are absent.',
  'strength': 2,
  'quote_verified': True},
 {'segment': 1,
  'theme': 'Domestic labour and the household',
  'evidence': 'I was feeling very shy, thinking I was walking in the street in broad '
              'daylight, but there was not a single man visible.',
  'note': "This passage highlights the domestic nature of the narrator's experience by "
          'describing her as walking alone on a street without men present.',
  'strength': 2,
  'quote_verified': True},
 {'segment': 1,
  'theme': "Narrator's doubt and the dream frame",
  'evidence': 'I am not sure whether I dozed off or not. But, as far as I remember, I '
              'was wide awake.',
  'note': 'This passage shows the narrator questioning her state of consciousness, '
          'which is a common feature in dream narratives.',
  'strength': 2,
  'quote_verified': True},
 {'segment': 2,
  'theme': 'Spatial segregation (zenana and mardana)',
  'evidence': 'But dear Sultana, how unfair it is to shut in the harmless women and '
              'let loose the men.',
  'note': 'This passage directly addresses the spatial segregation of women in the '
          'zenana and men in the mardana, which is a central theme in the story.',
  'strength': 3,
  'quote_verified': True},
 {'segment': 2,
  'theme': 'Reversal of gender roles',
  'evidence': 'We have no hand or voice in the management of our social affairs. In '
              'India man is lord and master, he has taken to himself all powers and '
              'privileges and shut up the women in the zenana.',
  'note': 'This passage shows a reversal of traditional gender roles by suggesting '
          'that men are in charge while women are confined to the zenana, which is '
          "central to the story's critique.",
  'strength': 3,
  'quote_verified': True},
 {'segment': 2,
  'theme': 'Domestic labour and the household',
  'evidence': 'We have nothing else to do in our zenana. I finish my work in two '
              'hours.',
  'note': 'This passage highlights the domestic labor performed by women, which is a '
          "central theme of the story's critique on gender roles and social "
          'structures.',
  'strength': 2,
  'quote_verified': False},
 {'segment': 2,
  'theme': 'Colonial and social context',
  'evidence': 'We have no hand or voice in the management of our social affairs. In '
              'India man is lord and master, he has taken to himself all powers and '
              'privileges and shut up the women in the zenana.',
  'note': 'This passage reflects the colonial and social context by critiquing the '
          'traditional gender roles imposed by colonial authorities on Indian society.',
  'strength': 2,
  'quote_verified': True},
 {'segment': 3,
  'theme': 'Spatial segregation (zenana and mardana)',
  'evidence': 'On the following day the Queen called upon all men to retire into '
              'zenanas for the sake of honour and liberty.',
  'note': "This passage directly mentions the use of 'zenanas' as a spatial "
          'arrangement, which is central to the purdah system being critiqued in the '
          'story.',
  'strength': 3,
  'quote_verified': True},
 {'segment': 3,
  'theme': 'Reversal of gender roles',
  'evidence': 'The Queen called upon all men to retire into zenanas for the sake of '
              'honour and liberty, reversing the traditional role of women as '
              'sequestered within purdah systems.',
  'note': 'This passage shows a reversal in the gendered division of space by having '
          "men enter the 'zenana' (purdah system), which is central to the critique of "
          'purdah being reversed through female empowerment and scientific '
          'achievement.',
  'strength': 3,
  'quote_verified': False},
 {'segment': 3,
  'theme': "Women's education and science",
  'evidence': 'Education was spread far and wide among women, and early marriage also '
              'was stopped. No woman was to be allowed to marry before she was '
              'twenty-one.',
  'note': 'This passage highlights the expansion of female education and control over '
          'marriage as part of the purdah system being critiqued, which is central to '
          'the reversal in gender roles discussed later in the story.',
  'strength': 3,
  'quote_verified': False},
 {'segment': 3,
  'theme': 'Critique of male governance and war',
  'evidence': 'The Queen refused to hand over the refugees to his officers, declaring '
              'that it was against her principle to turn out refugees. For this '
              'refusal the king declared war against our country.',
  'note': 'This passage shows a critique of male-dominated military power and '
          "governance through the Queen's refusal to surrender refugees, which is "
          'central to the reversal in gender roles discussed later in the story.',
  'strength': 3,
  'quote_verified': False},
 {'segment': 3,
  'theme': 'Domestic labour and the household',
  'evidence': 'The Lady Principal with her two thousand students marched to the battle '
              'field, and arriving there directed all the rays of the concentrated '
              'sunlight and heat towards the enemy.',
  'note': 'This passage shows a reversal in domestic roles by having women take on '
          'military responsibilities, which is central to the critique of purdah being '
          'reversed through female empowerment and scientific achievement.',
  'strength': 3,
  'quote_verified': True},
 {'segment': 3,
  'theme': 'Technology and nature',
  'evidence': 'They invented an instrument by which they could collect as much '
              'sun-heat as they wanted. And they kept the heat stored up to be '
              'distributed among others as required.',
  'note': 'This passage shows a technological advancement in collecting and '
          'distributing solar energy, which is central to the critique of '
          'male-dominated military power being reversed through female empowerment and '
          'scientific achievement.',
  'strength': 3,
  'quote_verified': True},
 {'segment': 3,
  'theme': 'Colonial and social context',
  'evidence': 'The enemy however, was too strong for them. Our soldiers fought '
              'bravely, no doubt. But in spite of all their bravery the foreign army '
              'advanced step by step to invade our country.',
  'note': 'This passage shows a critique of colonial military power through the '
          'depiction of male-dominated military forces being defeated by female-led '
          'scientific achievements, which is central to the reversal in gender roles '
          'discussed later in the story.',
  'strength': 3,
  'quote_verified': True},
 {'segment': 3,
  'theme': "Narrator's doubt and the dream frame",
  'evidence': 'How did you manage to gather and store up the sun-heat? I asked her in '
              'amazement.',
  'note': "This passage shows a narrator questioning Sultana's ability to perform an "
          'action, which is central to the reversal of gendered division of space '
          'being questioned through female empowerment and scientific achievement.',
  'strength': 2,
  'quote_verified': False},
 {'segment': 4,
  'theme': 'Spatial segregation (zenana and mardana)',
  'evidence': 'Since the "Mardana" system has been established, there has been no more '
              'crime or sin; therefore we do not require a policeman to find out a '
              'culprit, nor do we want a magistrate to try a criminal case.',
  'note': 'This passage indicates that the establishment of the Mardana system has led '
          'to a reduction in crime and the elimination of police and magistrates, '
          'suggesting a change in spatial segregation between different social roles.',
  'strength': 2,
  'quote_verified': True},
 {'segment': 4,
  'theme': 'Reversal of gender roles',
  'evidence': 'Our noble Queen is exceedingly fond of botany; it is her ambition to '
              'convert the whole country into one grand garden.',
  'note': 'This passage shows that women, particularly the Queen, are involved in '
          'activities traditionally associated with men, such as gardening and '
          'scientific pursuits, reversing traditional gender roles.',
  'strength': 3,
  'quote_verified': True},
 {'segment': 4,
  'theme': 'Domestic labour and the household',
  'evidence': 'We have no rail road nor any paved streets here. Therefore neither '
              'street nor railway accidents occur here.',
  'note': 'This passage highlights the lack of infrastructure, such as railways and '
          'paved roads, which implies a focus on domestic labor and the efficient '
          'management of everyday tasks within the household.',
  'strength': 2,
  'quote_verified': False},
 {'segment': 4,
  'theme': "Narrator's doubt and the dream frame",
  'evidence': 'And before I could realize that we had commenced moving, we reached the '
              'garden of the Queen. The idea is excellent. What is your chief food?',
  'note': "This passage shows the narrator's confusion about their sudden transition "
          'from a dream to reality, indicating the use of a dream frame in the '
          'narrative.',
  'strength': 1,
  'quote_verified': False}]
