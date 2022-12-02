import random

alphbet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def shuffle(alphabet):
    key = list(alphabet)
    random.shuffle(key)
    key_str = ''
    for i in key:
        key_str += str(i)
    return key_str


def coding():
    string = input('Введите открытый текст:')
    string = string.upper()
    coded_string = ''
    key = shuffle(alphbet)
    print('Ваш ключ:' + str(key))
    for i in string:
        coded_string += key[alphbet.index(i)]
    return 'Шифртекст:' + coded_string


def encoding():
    coded_string = input('Введите шифр текст:')
    decoded_string = ''
    key = input('Введите ключ:')
    for i in coded_string:
        decoded_string += alphbet[key.index(i)]
    return 'Открытый текст:' + decoded_string

# PKYUWCQLWZKLGHQWJFKLBRYGYKLFQLSWLSJQGUGUBCYGYBCAMCQYWCBHYUWYUXWLYRCAMKGDBCLQLLWMNWKJKLFQLKLFFQWFQLGUWQGYUWKRYUBCBHKLRZDWCBHWTXWJJWLYGUBCYGYBCQWGMUQXUFWKJMQYUURZKLLKYRCWKLFIGAXUBJBSAKYYUWKSWBHWQSUYWWLGUWFWXQFWFYBDWXBZWKICBHWGGQBLKJMCQYWCUWCHQCGYGUBCYGYBCQWGKIIWKCWFQLZWJDBRCLWQLDRYJQYWCKCAHKZWXKZWYBUWCQLJBLFBLKHYWCYUWIRDJQXKYQBLBHKXBJJWXYQBLBHGUBCYGYBCQWGXKJJWFQLKSWCZKLIWLGQBLPKYUWCQLWZKLGHQWJFYBBPKSCWKYQLYWCWGYQLCRGGQKLJQYWCKYRCWIKCYQXRJKCJAQLYUWMBCPGBHXUWPUBEQLHKXYGUWXBLGQFWCWFUWCGWJHYBDWKIRIQJBHYUWSCWKYCRGGQKLMCQYWCCBGWZKCAHWJJMKGLBYWTKXYJADWKRYQHRJGUWMKGABRLSDCQJJQKLYWTYCWZWJAZBFWCLMWJJFCWGGWFKLFKZKNQLSJAMWJJCWKFQLYUWLWMWGYBHYUWLWMDBBPGCBGWZKCAUKFDWWLZKCCQWFYMBAWKCGKLFUWCURGDKLFMKGEWCAHBLFBHUWCYUWAMWCWCQXUCWKJJACQXULBYORGYXBZHBCYKDJAMWJJBHHGBQHCBGWZKCAMKLYWFYBGUBIGUWMBRJFSBYBIKCQGKGABRKLFQMBRJFSBYBDBLFGYCWWYBLWMQLYWCKHYWCLBBLGUWMWLYQLYBKGZKJJGUBIYBJBBPKYKJQYYJWDBTMUQXUYUWGUBIZKLUKFDWWLPWWIQLSHBCUWCUWUKFGUBMLQYYBLBDBFAKGAWYGBYUKYGUWZQSUYDWYUWHQCGYYBGWWQYXUKCZQLSCBGWZKCAKFZQCWFYUWDBTDRYUBMZRXUMBRJFUWXUKCSWUWCHBCQYHBCKZBZWLYYUWGUBIZKLFQFLBYGWWZYBUWKCYUWJKFAXBRJFXWCYKQLJAKHHBCFKUQSUICQXWYUWLUQGMBCFGCWKXUWFUWCYMWLYAWQSUYSRQLWKGZKFKZYMWLYAWQSUYSRQLWKGCBGWZKCASKEWLBGQSLWEWLQHBLWQGCQXUUWCEBQXWMKGFCWKZAKGGUWKLGMWCWFMWJJPWWIQYHBCZWMQJJABRQJJYUWGUBIZKLDBMWFUWMBRJFDWMQJJQLSBHXBRCGWYBPWWIQYHBCUWCHBCWEWCBRYGQFWCKQLMKGHKJJQLSYUWCWMKGKXBJFDQYYWCYKGYWQLYUWKQCKLFYUWLWMJAJQSUYWFJKZIGJBBPWFGKFKYYUKYEWCAZBZWLYKABRLSSQCJYUQLFKCPKIIWKCWFKYCBGWZKCAGWJDBMKLFKEBQXWJQPWKGQSUDCWKYUWFZKFKZZKAQGIWKPYBABRKZBZWLYGIWKPYBZWCBGWZKCAYRCLWFGUWGKMKJQYYJWXCWKYRCWLBBJFWCYUKLUWCGWJHMUBGUQEWCWFKGYUBRSUGUWUKFORGYXBZWBRYBHYUWMKYWCZKFKZXKZWYUWEBQXWMBRJFABRJWYZWUKEWYUWICQXWBHKXRIBHYWKKXRIBHYWKYUWCWMKGGBZWYUQLSGQZIJWGQLXWCWQLYUKYEBQXWQYXBRJFLYDWYUWEBQXWBHKDWSSKCYUWLUKEWABRLBZBLWAKYKJJKGPWFCBGWZKCALBLWZKFKZXKZWYUWKLGMWCUBMRLRGRKJCBGWZKCAJBBPWFKYYUWSQCJXJBGWCKLFGRFFWLJAQYGWWZWFYBUWCGRXUKLKFEWLYRCWGRIIBGQLSGUWYBBPYUWSQCJUBZWGRIIBGQLSGUWFQFBLWBHYUBGWYUQLSGGUWMKGKJMKAGCWKFQLSKDBRYBCGWWQLSBLYUWGYKSWMUKYMBRJFUKIIWLQYMBRJFDWYUCQJJQLSKLFGUWUWKCFUWCGWJHGKAQLSKHYWCMKCFGYBYUWKZKNWZWLYBHUWCHCQWLFGQGQZIJAYBBPUWCUBZWMQYUZWKLFGUWGYWIIWFHBCMKCFKLFGKQFYBYUWSQCJDWGQFWUWCXBZWUBZWYBYWKMQYUZWYUWSQCJSKEWKGYKCYABRCWABRCWLBYYKPQLSZWYBYUWIBJQXWGYKYQBLYUWCWMKGIKQLQLUWCEBQXWYUWIBJQXWGYKYQBLCBGWZKCAJKRSUWFBRYMUAGUBRJFQDWGBXCRWJLBQBLJAMKLYYBZKPWABRMKCZKLFYBUWKCKLAYUQLSABRXKCWYBYWJJZWXBZWKJBLSURLSCAIWBIJWKCWWKGQJAJWFYUWHBBYZKLUWJFYUWFBBCBHYUWXKCBIWLKLFKZBZWLYJKYWCYUWAMWCWCQFQLSYUCBRSUYUWFRGPYUWCWXCQWFCBGWZKCAKGYUWACWKXUWFUWCDWKRYQHRJDQSDWFCBBZXBZWKLFGQYFBMLGUWGKQFIRJJQLSUWCDQSXUKQCRIYBYUWHQCWXBZWKLFSWYMKCZABRJBBPGBYWCCQDJAXBJFQFKCWLYZKFKZUWGQYKYWFYUWSQCJBUIJWKGWCBGWZKCACKLHBCMKCFABRZRGYLYDWHCQSUYWLWFABRZRGYLYCWKJJAKLFSWLYJAGUWUKJHIRGUWFYUWYUQLHQSRCWQLYBYUWXUKQCYUWCWMKGKMUQGIWCYUKYGBRLFWFJQPWEWCASBBFZKFKZKLFYUWMBCLUKYMKGYKPWLBHHKLFJWYZWUWJIABRBHHMQYUABRCXBKYYBBGKQFCBGWZKCAYUWSQCJGYBBFRIDRYGUWUWJFBLYBYUWXUKQCMQYUBLWUKLFKLFJWYCBGWZKCAIRJJYUWLGUWGKQFVRQXPJADRYGBJQSUYJAKLFGYCKLSWJAQZEWCAGBCCAZKFKZDRYQZSBQLSYBHKQLYQGUKJJHKJJZKFKZQHQFBLYUKEWGBZWYUQLSSBBFUWKEWLGUBMYUBRSUYJWGGQKZCBGWZKCACRGUWFYBYUWDWJJYWKYWKKYBLXWKLFGBZWDCKLFAQZZWFQKYWJAYUWZKQFMKGSBLWKLFYUWSQCJKJZBGYDRCGYQLYBYWKCGGUWHBCSBYYBDWGUAHBCSBYWEWCAYUQLSWTXWIYYUKYYUWAMWCWDBYUMBZWLKLFXCQWFBRYQXKLYSBBLKLAJBLSWCJQPWYUQGQXKLYGYKLFQYQMQGUQMWCWFWKFQCWKJJAXKLYGYKLFQYABRMBLYUKEWYBQJJJBBPKHYWCABRQJJKCCKLSWGBZWYUQLSFBGYBIXCAQLSIJWKGWYUWBYUWCFQFGYBIORGYQLYQZWHBCCBGWZKCAYBSWYRIDWHBCWYUWYWKXKZWKLFCWKJJAYUWWHHWXYBHYUKYGJQSUYZWKJMKGKZKNQLSMUWLYUWYWKYKDJWMKGXKCCQWFKMKAKLWMSQCJKJQSUYXCWKYRCWMQYUFKCPJQIGKLFFWWIWAWGJKADKXPQLYUWDQSXUKQCKYYUKYZBZWLYYUWFBBCUKLFJWYRCLWFCBGWZKCAXKLQXBZWQLQYMKGIUQJQIUWCURGDKLFBHXBRCGWUWXKZWQLBUQZGBGBCCAUWGKQFKGQHKIBJBSQNQLSKLFGYBIIWFKLFGYKCWFQYGVRQYWKJJCQSUYGKQFCBGWZKCAGZQJQLSYUQGQGZAHCQWLFZQGGGZQYUZKFKZGKQFYUWHQSRCWQLYUWXUKQCGZQYUGKQFCBGWZKCAMWKCWSBQLSYBUKEWKJQYYJWYKJPIUQJQIGZQJWFUQGXUKCZQLSGZQJWKGKZKYYWCBHHKXYUWGKQFQMKLYWFABRYBXBZWQLYBYUWJQDCKCAHBCKZBZWLYMQJJZQGGGZQYUWTXRGWRGYUWDQSWAWGMWCWCKQGWFYBUQZDRYCBGWZKCAKLGMWCWFHBCUWCBHXBRCGWGUWMQJJKLFYUWAMWLYBRYBHYUWCBBZYBSWYUWCQGKAGKQFIUQJQIMUWLYUWAMWCWKJBLWWTIJKQLMUBQGGUWMUKYFBWGQYKJJZWKLCBGWZKCAJKRSUQLSJWKLWFKSKQLGYYUWFBBCKLFGKQFQIQXPWFUWCRIQLYUWGYCWWYCWKJJAGUWKGPWFZWHBCYUWICQXWBHKXRIBHYWKKLFQDCBRSUYUWCUBZWMQYUZWXBLSCKYRJKYQBLGIUQJQIGBRLFWFKGYUBRSUUWMWCWOBPQLSDRYMUKYBLWKCYUKCWABRSBQLSYBFBMQYUUWCDWLQXWYBUWCGKQFCBGWZKCAVRQXPJAJBBPKHYWCUWCQFBLYPLBMUBMMWUKEWLYYKJPWFAWYORGYGUBMUWCYCWKYUWCZKPWUWCHWWJDRYGKQFIUQJQIGJBMJAKLFUWXRYYUWWLFBHKXQSKCGUWGGBWTYCWZWJAICWYYAGUWXKLYDWZBCWYUKLYMWLYAICWYYACBGWZKCAMKGGBGRCICQGWFYUKYGUWDJRGUWFFBABRYUQLPGBQQUKFLYYUBRSUYKDBRYQYSBBFJBCFIUQJQIYBBPKZKYXUGUWGKDGBJRYWJAJBEWJAJBBPKSKQLZAXUQJFDRYJWYZWPLBMQHZQGGGZQYUQGSBQLSYBFQLWMQYURGABRKDGRCFXCWKYRCWGKQFCBGWZKCAKLFGUWMWLYBRYBHYUWJQDCKCADRYLBYDKXPYBUWCDWFCBBZGUWMWLYYBUWCMCQYQLSCBBZKLFGKYFBMLKYUWCFWGPICWYYAKDGBJRYWJAJBEWJAUWCUWKCYDWKYJQPWKUWKEADWJJGUWBIWLWFKFCKMWCYBBPBRYHQEWIBRLFLBYWGJBBPWFKYYUWZIRYYMBDKXPKLFUBJFQLSYUWYUCWWQLUWCUKLFMWLYDKXPYBUWCDWFCBBZUKJHKLUBRCJKYWCIUQJQIMKGGYQJJQLYUWJQDCKCAMUWLCBGWZKCAXKZWQLQBLJAMKLYWFYBYWJJABRGKQFGUWKLFGUWJWKLWFKSKQLGYYUWFBBCKSKQLZQGGGZQYUMBLYFQLWMQYURGYBLQSUYIUQJQIIRYFBMLYUWIKIWCBUMUKYGUKIIWLWFICWEQBRGWLSKSWZWLYCBGWZKCAXKZWBEWCKLFGKYFBMLBLUQGPLWWGUWQLGQGYWFBLSBQLSGUWGKQFGBQSKEWYUWIBBCJQYYJWYUQLSKICWGWLYBHZBLWAQXBRJFLYPWWIUWCKSKQLGYUWCMQJJXBRJFQGUWKFFWFGBHYJAYUWCWMKGKIKRGWYUWLCBGWZKCAGKQFFCWKZQJAQGKMKMBLFWCHRJJQYYJWDBTYBFKAQYXBGYYMWLYAWQSUYSRQLWKGXKLQUKEWQYABRXKLJQYYJWMKGYWHRJBLWGKQFUWABRPLBMQXKLYFWLAABRKLAYUQLSDRYYUKYMKGLBYCWKJJAMUKYCBGWZKCAMKLYWFYBGKAIUQJQIGUWMUQGIWCWFKZQICWYYA
# KDXFWHSUQVPJZLBIOCGYREMTAN
print(coding())
