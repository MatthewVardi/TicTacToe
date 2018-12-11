import pprint

message = '''Lorem ipsum dolor sit amet, ei brute causae efficiantur vix. His in facer altera, pri ne possim accusata intellegat. Eius facer labores id duo, ius cu iudico aeterno percipit. Feugait gubergren in pri. Ut elitr albucius mea.

Justo elitr libris te eum, vix et dicta maiorum, duis sententiae id ius. Et sanctus blandit legendos cum, ne hinc invidunt philosophia nam, no his commodo disputando. Sanctus volutpat ea duo, vel ad ferri antiopam tincidunt, vim purto iudico an. Civibus deleniti apeirian nam no, in sit laoreet necessitatibus, duo in tale latine assueverit. Sea modo cetero voluptatibus ut, soleat persecuti vim at. Fugit etiam vivendo has ad.

Per no sonet alienum oporteat. At per inimicus salutatus. Ei eius consequuntur nec. Error deseruisse qui cu, sed zril noster salutatus ut, quot scribentur et vis. Impetus vivendo id nec.

Usu movet accusamus cu, eu sea quod impetus scripta. Pro everti invenire ex, eam periculis similique voluptatum in, usu stet labore equidem cu. His id voluptua assueverit, ut est quando consequat consequuntur. Ei vis essent option complectitur, mei debet elitr phaedrum ut, cu vidit harum maiestatis per.

Pro laudem percipit constituto ut, ea vim agam iusto impetus, quo appetere mnesarchum an. Mea id primis verterem conceptam, eu nec vitae ridens evertitur, nec in doctus necessitatibus. Verear pertinax eu vix, nec ad veniam dissentiet. Duis eleifend adipiscing pro et. Et velit dicta regione mel, in accumsan placerat euripidis usu. No impedit erroribus temporibus est, meis consequat ad duo, id omnis legimus iracundia nec.'''
count = {}

for character in message.upper():
	count.setdefault(character, 0) # default the dictionary to have 0 of each letter
	count[character] = count[character] + 1 # increment if found letter in that index 


text = pprint.pformat(count)
print(text)

#pprint for pretty print
#pformat allows to set it to a string variable 