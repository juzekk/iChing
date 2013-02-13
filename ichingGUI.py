#-*- coding: utf-8 -*-

import random
import Tkinter


iching={
'XXXXXX':1,'OOOOOO':2,'XOOOXO':3,'OXOOOX':4,
'XXXOXO':5,'OXOXXX':6,'OXOOOO':7,'OOOOXO':8,
'XXXOXX':9,'XXOXXX':10,'XXXOOO':11,'OOOXXX':12,
'XOXXXX':13,'XXXXOX':14,'OOXOOO':15,'OOOXOO':16,
'XOOXXO':17,'OXXOOX':18,'XXOOOO':19,'OOOOXX':20,
'XOOXOX':21,'XOXOOX':22,'OOOOOX':23,'XOOOOO':24,
'XOOXXX':25,'XXXOOX':26,'XOOOOX':27,'OXXXXO':28,
'OXOOXO':29,'XOXXOX':30,'OOXXXO':31,'OXXXOO':32,
'OOXXXX':33,'XXXXOO':34,'OOOXOX':35,'XOXOOO':36,
'XOXOXX':37,'XXOXOX':38,'OOXOXO':39,'OXOXOO':40,
'XXOOOX':41,'XOOOXX':42,'XXXXXO':43,'OXXXXX':44,
'OOOXXO':45,'OXXOOO':46,'OXOXXO':47,'OXXOXO':48,
'XOXXXO':49,'OXXXOX':50,'XOOXOO':51,'OOXOOX':52,
'OOXOXX':53,'XXOXOO':54,'XOXXOO':55,'OOXXOX':56,
'OXXOXX':57,'XXOXXO':58,'OXOOXX':59,'XXOOXO':60,
'XXOOXX':61,'OOXXOO':62,'XOXOXO':63,'OXOXOX':64
}
nazwaHex={
1:' 乾 (qián), Siła',2:'坤 (kūn), Pole',3:'屯 (chún), Kiełkowanie',4:'蒙 (méng), Oskrzydlający',
5:'需 (xū), Przystępujący',6:'訟 (sòng), Kłócący się',7:'師 (shī), Przewodzący',8:'比 (bǐ), Grupujący',
9:'小畜 (xiǎo chù), Kumulujący maluczkich',10:'履 (lǚ), Stąpający',11:'泰 (tài), Przenikający',12:'否 (pǐ), Obstrukcja',
13:'同人 (tóng rén), Pojednujący ludzi',14:'大有 (dà yǒu), Wielkie posiadanie',15:'謙 (qiān), Korzący',16:'豫 (yù), Utrzymujący',
17:'隨 (suí), Podążający',18:'蠱 (kŭ), Psujący',19:'臨 (lín), Zbliżający',20:'觀 (guān), Oglądający',
21:'噬嗑 (shì kè), Rozdzierające ugryzienie',22:'賁 (bì), Zdobiący',23:'剝 (bō), Zdzierający',24:'復 (fù), Powracający',
25:'無妄 (wú wàng), Bez zaangażowania',26:'大畜 (dà chù), Wielce akumulujący',27:'頤 (yí), Połykający',28:'大過 (dà guò), Wielce przekraczający',
29:'坎 (kǎn), Otchłań',30:'離 (lí), Blask',31:'咸 (xián), Kojarzący',32:'恆 (héng), Nieustawający',
33:'遯 (dùn), Wycofujący',34:'大壯 (dà zhuàng), Wielce wzmacniający',35:'晉 (jìn), Prosperujący',36:'明夷 (míng yí), Zaciemniający światło',
37:'家人 (jiā rén), Mieszkający ludzie',38:'睽 (kuí), Polaryzujący',39:'蹇 (jiǎn), Utykający',40:'解 (xiè), Rozdzielający',
41:'損 (sǔn), Zanikający',42:'益 (yì), Powiększający',43:'夬 (guài), Dzielący',44:'姤 (gòu), Kojarzący w pary',
45:'萃 (cuì), Skupiający',46:'升 (shēng), Pnący się',47:'困 (kùn), Krępujący',48:'井 (jǐng), Dążący do źródła',
49:'革 (gé), Obdzierający ze skóry',50:'鼎 (dǐng), Trzymający',51:'震 (zhèn), Wstrząs',52:'艮 (gèn), Ograniczenie',
53:'漸 (jiàn), Infiltrujący',54:'歸妹 (guī mèi), Nawracający dziewicę',55:'豐 (fēng), Bycie w obfitości',56:'旅 (lǚ), Goszczący',
57:'巽 (xùn), Grunt',58:'兌 (duì), Otwarty',59:'渙 (huàn), Rozwiewający',60:'節 (jié), Wyrażający',
61:'中孚 (zhōng fú), Wracający do środka',62:'小過 (xiǎo guò), Nieznacznie wykraczający',63:'既濟 (jì jì), Już forsujący bród',64:'未濟 (wèi jì), Jeszcze nie brodzący'
}
obraz={
1:'TWORZĄCY przynosi najwyższe szczęście. Korzystna jest stałość.',
2:'PRZYJMUJĄCA przynosi najwyższe szczęście. Korzystna jest stałość klaczy. Człowiek szlachetny - gdy coś podejmie - pragnąc przewodzić zbłądzi, idąc śladem znajdzie przewodnika. Korzystne jest szukać przyjaciół na zachodzie i południu, zaś uczniów i podwładnych na wschodzie i północy. Spokojna stałość przynosi szczęście.',
3:'POCZĄTKOWE TRUDNOŚCI dają najwyższy sukces. Korzystna jest stałość. Nie powinien niczego przedsiębrać. Korzystne jest ustanowienie pomocników.',
4:'MŁODZIEŃCZE NIEDOŚWIADCZENIE przynosi sukces. Nie szukam niedoświadczonego: to on mnie szuka. Pouczam go pierwszą wyrocznią. Pytając raz, drugi i trzeci objawia natręctwo. Natręta więcej nie pouczam. Korzystna jest stałość.',
5:'Jeśli jest szczery, osiąga światło i sukces. Stałość przynosi szczęście. Korzystne będzie przekroczenie wielkiej wody.',
6:'Jest szczery, lecz mimo to napotyka przeciwności. Ostrożne zatrzymanie się wśród drogi przynosi szczęście. Dążenie do końca przynosi nieszczęście. Korzystne będzie spotkać się z wielkim człowiekiem. Niekorzystne będzie przekroczenie wielkiej wody.',
7:'WOJSKO wymaga wytrwałości i silnego człowieka. Szczęście bez winy.',
8:'ZWIĄZEK przynosi szczęście. Zapytaj wyroczni raz jeszcze, czy masz dość szlachetności, stałości i wytrwałości. Wówczas nie ma winy. Niepewni dołączą stopniowo. Nieszczęście spotka tego, który przyjdzie zbyt późno.',
9:'Sukces. Gęste chmury, nie ma deszczu z zachodnich regionów.',
10:'Stąpa po ogonie tygrysa, który go nie kąsa. Sukces.',
11:'Małe odchodzi, wielkie nadchodzi. Szczęście. Sukces.',
12:'Szukanie związku ze złymi ludźmi nie jest korzystne dla człowieka szlachetnego, choćby zachował stałość.',
13:'WSPÓLNOTA w otwartości. Sukces. Korzystne będzie przekroczenie wielkiej wody. Korzystna jest stałość szlachetnego.',
14:'Ogień ponad niebem: obraz OBFITOŚCI. Człowiek szlachetny powstrzymuje zło i wspomaga dobro, posłuszny dobroczynnej woli nieba.',
15:'UMIARKOWANIE prowadzi do sukcesu. Człowiek szlachetny doprowadza sprawy do końca.',
16:'Korzystne jest zgromadzenie zwolenników i pchnięcie armii naprzód.',
17:'IŚĆ ŚLADEM przynosi najwyższy sukces. Korzystna jest stałość. Bez winy.',
18:'NAPRAWIANIE ZNISZCZEŃ daje najwyższe szczęście. Korzystne będzie przekroczenie wielkiej wody. Trzy dni przed rozpoczęciem, trzy dni po rozpoczęciu.',
19:'ZBLIŻENIE oznacza najwyższe szczęście. Korzystna jest stałość. Nieszczęście, gdy przeważy osiem.',
20:'Dokonano ablucji, lecz jeszcze nie złożono ofiar. Wpatrują się w niego, pełni ufności.',
21:'PRZEGRYZANIE przynosi szczęście. Korzystne, gdy sprawiedliwości staje się zadość.',
22:'WDZIĘK przynosi sukces. W małych sprawach korzystne jest przedsięwziąć cokolwiek.',
23:'Nie przynosi korzyści ruch w jakimkolwiek kierunku.',
24:'Sukces. Wychodzi i powraca bez błędu. Przybywają przyjaciele bez winy. Droga wiedzie tam i z powrotem. Siódmego dnia zwrot. Korzystne jest mieć dokąd pójść.',
25:'Najwyższy sukces. Korzystna jest stałość. Jeśli nie jest takim, jakim być powinien, dozna nieszczęścia i nie wyjdzie mu na korzyść nic, co przedsięweźmie.',
26:'Korzystna jest stałość. Szczęście, gdy nie jada w domu. Korzystne będzie przekroczenie wielkiej wody.',
27:'Stałość przynosi szczęście. Zwraca uwagę na dostarczanie pożywienia i na to czego szuka, by wypełnić usta.',
28:'Belka podtrzymująca sklepienie wygina się, bliska złamania. Korzystne jest mieć dokąd pójść. Sukces.',
29:'Podwójnie NIEZGŁĘBIONY. Jeśli jest szczery, nosi sukces w sercu. Wiedzie mu się we wszystkim, co robi.',
30:'Korzystna jest stałość. Przynosi sukces. Troska o krowę przynosi szczęście.',
31:'Sukces. Korzystna jest stałość. Szczęście, gdy pojmie pannę za żonę.',
32:'Sukces. Bez winy. Korzystna jest stałość. Korzystne jest mieć dokąd pójść.',
33:'Sukces. W rzeczach małych korzystna jest stałość.',
34:'Korzystna jest stałość.',
35:'Potężnego księcia czczą wielką liczbą koni. W jednym dniu trzykrotnie podejmowany jest u dworu.',
36:'Wśród przeciwieństw korzystna jest stałość.',
37:'Korzystna jest stałość kobiety.',
38:'Szczęście w sprawach małych.',
39:'Korzystne na południowym zachodzie, niekorzystne na północnym wschodzie. Korzystne jest spotkać się z wielkim człowiekiem. Stałość przynosi szczęście.',
40:'Korzystne na południowym zachodzie. Gdy już nie musi nigdzie iść, powrót przynosi szczęście. Gdy wciąż jeszcze musi gdzieś iść, pośpiech przynosi szczęście.',
41:'POMNIEJSZENIE w połączeniu z prostotą daje najwyższe szczęście. Bez winy. Może być w tym stały. Korzystne jest przedsięwzięcie czegoś. Jak można go dokonać? Może użyć dwóch małych miseczek ofiarnych.',
42:'Korzystne jest przedsięwzięcie czegoś. Korzystne jest przekroczenie wielkiej wody.',
43:'Należy zdecydowanie objawić sprawy na królewskim dworze. Muszą być objawione wiarygodnie. Niebezpieczeństwo. Należy ostrzec swoje miasto. Użycie broni nie da korzyści. Korzystne jest coś przedsięwziąć.',
44:'Panna jest potężna, nie należy się żenić z taką panną.',
45:'Sukces. Król zbliża się do świątyni. Korzystne będzie spotkać się z wielkim człowiekiem: przynosi sukces. Korzystna jest stałość. Składanie wielkich ofiar buduje szczęście. Korzystne jest przedsięwzięcie czegokolwiek.',
46:'WZRASTANIE niesie najwyższy sukces. Musi zobaczyć się z wielkim człowiekiem. Bez lęku. Odjazd na południe przynosi szczęście.',
47:'Sukces. Stałość. Wielki człowiek przynosi szczęście. Bez winy. Jeżeli ma się coś do powiedzenia nie dadzą temu wiary.',
48:'ożna przenieść miasto, nie można przenieść studni. Nie zmniejsza się, ani nie rośnie. Przychodzi, odchodzi, ciągnie ze studni. Już prawie dosięga wody, ale nie starcza sznura lub rozbija się dzban. Nadchodzi nieszczęście.',
49:'Ogień nad drzewem: obraz NACZYNIA OFIARNEGO. Człowiek szlachetny konsoliduje swój los nieustannie korygując pozycję.',
50:'Najwyższe szczęście. Sukces.',
51:'Grom przynosi sukces. Grom przychodzi: „Och, och!” Potem śmiech: „Cha, cha!” Grom przeraża na sto mil, ale nie pozwala, by spadły ofiarne łyżki i kielichy.',
52:'Wstrzymuje plecy i nie czuje już swego ciała. Wychodzi na podwórze i nie widzi już towarzyszy. Bez winy.',
53:'Wydają za mąż pannę młodą. Szczęście. Korzystna jest stałość.',
54:'Przedsięwzięcia przynoszą nieszczęście. Nic co byłoby korzystne.',
55:'Obfitość niesie sukces. Król osiąga obfitość. Nie bądź smutny! Bądź jak słońce w południe.',
56:'Sukces przez to, co małe. Stałość przynosi szczęście wędrowcowi.',
57:'Sukces dzięki temu, co małe. Korzystne, gdy ma dokąd pójść. Korzystne jest zobaczyć się z wielkim człowiekiem.',
58:'Sukces. Korzystna jest stałość.',
59:'Sukces. Król zbliża się do świątyni. Korzystne jest przekroczenie wielkiej wody. Korzystna jest stałość.',
60:'Dręczące ograniczenia nie mogą trwać uporczywie.',
61:'Świnie i ryby. Szczęście. Korzystne jest przekroczenie wielkiej wody. Korzystna jest stałość.',
62:'Sukces. Korzystna jest stałość. Można dokonać małych rzeczy, nie powinno się dokonywać wielkich rzeczy. Lecący ptak przynosi przesłanie: niedobrze jest dążyć wzwyż, trzeba pozostać na dole! Wielkie szczęście.',
63:'Sukces w małych sprawach. Korzystna jest stałość. Na początku szczęście, na końcu zamęt.',
64:'Sukces. Jeśli młody lis, który już przeszedł rzekę zmoczy ogon w wodzie, nic nie będzie korzystne.'
}
osad={
1:'Niebo nad niebem: ruch pełen potęgi. Człowiek szlachetny staje się silny i niezwyciężony.',
2:'PRZYJMUJĄCA przynosi najwyższe szczęście. Korzystna jest stałość klaczy. Człowiek szlachetny - gdy coś podejmie - pragnąc przewodzić zbłądzi, idąc śladem znajdzie przewodnika. Korzystne jest szukać przyjaciół na zachodzie i południu, zaś uczniów i podwładnych na wschodzie i północy. Spokojna stałość przynosi szczęście.',
3:'POCZĄTKOWE TRUDNOŚCI dają najwyższy sukces. Korzystna jest stałość. Nie powinien niczego przedsiębrać. Korzystne jest ustanowienie pomocników.',
4:'MŁODZIEŃCZE NIEDOŚWIADCZENIE przynosi sukces. Nie szukam niedoświadczonego: to on mnie szuka. Pouczam go pierwszą wyrocznią. Pytając raz, drugi i trzeci objawia natręctwo. Natręta więcej nie pouczam. Korzystna jest stałość.',
5:'Jeśli jest szczery, osiąga światło i sukces. Stałość przynosi szczęście. Korzystne będzie przekroczenie wielkiej wody.',
6:'Jest szczery, lecz mimo to napotyka przeciwności. Ostrożne zatrzymanie się wśród drogi przynosi szczęście. Dążenie do końca przynosi nieszczęście. Korzystne będzie spotkać się z wielkim człowiekiem. Niekorzystne będzie przekroczenie wielkiej wody.',
7:'WOJSKO wymaga wytrwałości i silnego człowieka. Szczęście bez winy.',
8:'ZWIĄZEK przynosi szczęście. Zapytaj wyroczni raz jeszcze, czy masz dość szlachetności, stałości i wytrwałości. Wówczas nie ma winy. Niepewni dołączą stopniowo. Nieszczęście spotka tego, który przyjdzie zbyt późno.',
9:'Sukces. Gęste chmury, nie ma deszczu z zachodnich regionów.',
10:'Stąpa po ogonie tygrysa, który go nie kąsa. Sukces.',
11:'Małe odchodzi, wielkie nadchodzi. Szczęście. Sukces.',
12:'Szukanie związku ze złymi ludźmi nie jest korzystne dla człowieka szlachetnego, choćby zachował stałość.',
13:'WSPÓLNOTA w otwartości. Sukces. Korzystne będzie przekroczenie wielkiej wody. Korzystna jest stałość szlachetnego.',
14:'Ogień ponad niebem: obraz OBFITOŚCI. Człowiek szlachetny powstrzymuje zło i wspomaga dobro, posłuszny dobroczynnej woli nieba.',
15:'UMIARKOWANIE prowadzi do sukcesu. Człowiek szlachetny doprowadza sprawy do końca.',
16:'Korzystne jest zgromadzenie zwolenników i pchnięcie armii naprzód.',
17:'IŚĆ ŚLADEM przynosi najwyższy sukces. Korzystna jest stałość. Bez winy.',
18:'NAPRAWIANIE ZNISZCZEŃ daje najwyższe szczęście. Korzystne będzie przekroczenie wielkiej wody. Trzy dni przed rozpoczęciem, trzy dni po rozpoczęciu.',
19:'ZBLIŻENIE oznacza najwyższe szczęście. Korzystna jest stałość. Nieszczęście, gdy przeważy osiem.',
20:'Dokonano ablucji, lecz jeszcze nie złożono ofiar. Wpatrują się w niego, pełni ufności.',
21:'PRZEGRYZANIE przynosi szczęście. Korzystne, gdy sprawiedliwości staje się zadość.',
22:'WDZIĘK przynosi sukces. W małych sprawach korzystne jest przedsięwziąć cokolwiek.',
23:'Nie przynosi korzyści ruch w jakimkolwiek kierunku.',
24:'Sukces. Wychodzi i powraca bez błędu. Przybywają przyjaciele bez winy. Droga wiedzie tam i z powrotem. Siódmego dnia zwrot. Korzystne jest mieć dokąd pójść.',
25:'Najwyższy sukces. Korzystna jest stałość. Jeśli nie jest takim, jakim być powinien, dozna nieszczęścia i nie wyjdzie mu na korzyść nic, co przedsięweźmie.',
26:'Korzystna jest stałość. Szczęście, gdy nie jada w domu. Korzystne będzie przekroczenie wielkiej wody.',
27:'Stałość przynosi szczęście. Zwraca uwagę na dostarczanie pożywienia i na to czego szuka, by wypełnić usta.',
28:'Belka podtrzymująca sklepienie wygina się, bliska złamania. Korzystne jest mieć dokąd pójść. Sukces.',
29:'Podwójnie NIEZGŁĘBIONY. Jeśli jest szczery, nosi sukces w sercu. Wiedzie mu się we wszystkim, co robi.',
30:'Korzystna jest stałość. Przynosi sukces. Troska o krowę przynosi szczęście.',
31:'Sukces. Korzystna jest stałość. Szczęście, gdy pojmie pannę za żonę.',
32:'Sukces. Bez winy. Korzystna jest stałość. Korzystne jest mieć dokąd pójść.',
33:'Sukces. W rzeczach małych korzystna jest stałość.',
34:'Korzystna jest stałość.',
35:'Potężnego księcia czczą wielką liczbą koni. W jednym dniu trzykrotnie podejmowany jest u dworu.',
36:'Wśród przeciwieństw korzystna jest stałość.',
37:'Korzystna jest stałość kobiety.',
38:'Szczęście w sprawach małych.',
39:'Korzystne na południowym zachodzie, niekorzystne na północnym wschodzie. Korzystne jest spotkać się z wielkim człowiekiem. Stałość przynosi szczęście.',
40:'Korzystne na południowym zachodzie. Gdy już nie musi nigdzie iść, powrót przynosi szczęście. Gdy wciąż jeszcze musi gdzieś iść, pośpiech przynosi szczęście.',
41:'POMNIEJSZENIE w połączeniu z prostotą daje najwyższe szczęście. Bez winy. Może być w tym stały. Korzystne jest przedsięwzięcie czegoś. Jak można go dokonać? Może użyć dwóch małych miseczek ofiarnych.',
42:'Korzystne jest przedsięwzięcie czegoś. Korzystne jest przekroczenie wielkiej wody.',
43:'Należy zdecydowanie objawić sprawy na królewskim dworze. Muszą być objawione wiarygodnie. Niebezpieczeństwo. Należy ostrzec swoje miasto. Użycie broni nie da korzyści. Korzystne jest coś przedsięwziąć.',
44:'Panna jest potężna, nie należy się żenić z taką panną.',
45:'Sukces. Król zbliża się do świątyni. Korzystne będzie spotkać się z wielkim człowiekiem: przynosi sukces. Korzystna jest stałość. Składanie wielkich ofiar buduje szczęście. Korzystne jest przedsięwzięcie czegokolwiek.',
46:'WZRASTANIE niesie najwyższy sukces. Musi zobaczyć się z wielkim człowiekiem. Bez lęku. Odjazd na południe przynosi szczęście.',
47:'Sukces. Stałość. Wielki człowiek przynosi szczęście. Bez winy. Jeżeli ma się coś do powiedzenia nie dadzą temu wiary.',
48:'ożna przenieść miasto, nie można przenieść studni. Nie zmniejsza się, ani nie rośnie. Przychodzi, odchodzi, ciągnie ze studni. Już prawie dosięga wody, ale nie starcza sznura lub rozbija się dzban. Nadchodzi nieszczęście.',
49:'Ogień nad drzewem: obraz NACZYNIA OFIARNEGO. Człowiek szlachetny konsoliduje swój los nieustannie korygując pozycję.',
50:'Najwyższe szczęście. Sukces.',
51:'Grom przynosi sukces. Grom przychodzi: „Och, och!” Potem śmiech: „Cha, cha!” Grom przeraża na sto mil, ale nie pozwala, by spadły ofiarne łyżki i kielichy.',
52:'Wstrzymuje plecy i nie czuje już swego ciała. Wychodzi na podwórze i nie widzi już towarzyszy. Bez winy.',
53:'Wydają za mąż pannę młodą. Szczęście. Korzystna jest stałość.',
54:'Przedsięwzięcia przynoszą nieszczęście. Nic co byłoby korzystne.',
55:'Obfitość niesie sukces. Król osiąga obfitość. Nie bądź smutny! Bądź jak słońce w południe.',
56:'Sukces przez to, co małe. Stałość przynosi szczęście wędrowcowi.',
57:'Sukces dzięki temu, co małe. Korzystne, gdy ma dokąd pójść. Korzystne jest zobaczyć się z wielkim człowiekiem.',
58:'Sukces. Korzystna jest stałość.',
59:'Sukces. Król zbliża się do świątyni. Korzystne jest przekroczenie wielkiej wody. Korzystna jest stałość.',
60:'Dręczące ograniczenia nie mogą trwać uporczywie.',
61:'Świnie i ryby. Szczęście. Korzystne jest przekroczenie wielkiej wody. Korzystna jest stałość.',
62:'Sukces. Korzystna jest stałość. Można dokonać małych rzeczy, nie powinno się dokonywać wielkich rzeczy. Lecący ptak przynosi przesłanie: niedobrze jest dążyć wzwyż, trzeba pozostać na dole! Wielkie szczęście.',
63:'Sukces w małych sprawach. Korzystna jest stałość. Na początku szczęście, na końcu zamęt.',
64:'Sukces. Jeśli młody lis, który już przeszedł rzekę zmoczy ogon w wodzie, nic nie będzie korzystne.'
}

class Hexagram():
    def __init__(self):
        self.linie=[]
        for i in range(6):
            self.linie.append('')
        self.generuj()

    def generuj(self):
        for i in range(5,-1,-1):
            self.linie[i]=random.choice(['X','O','X','O'])

    def wypisz(self):
        for i in range(6):
            if self.linie[i]=='X':
                print '--------'
            else:
                print '--- ---'

    def wyczytaj(self):
        kod=''
        for i in range(5,-1,-1):
            kod+=self.linie[i]
        return kod

    def numer(self):
        return iching[self.wyczytaj()]

    def nazwaH(self):
        return nazwaHex[self.numer()]

    def obraz(self):
        return obraz[self.numer()]

    def osad(self):
        return osad[self.numer()]

def testuj(ile): 

    for i in range(ile):
        h=Hexagram()
    # h.generuj()
    print "Hexagram=",h.wyczytaj()
    h.wypisz()
    try:
        print iching[h.wyczytaj()]
        h.nazwaH()
        h.obraz()
        h.kom()

    except KeyError:
        print 'Nie ma takiego klucza'

    
def testujGUI():
    def gener():
        h=Hexagram()
        #print(h.nazwaH())
        t.delete('1.0','500.0')
        o.delete('1.0','500.0')
        k.delete('1.0','500.0')
        t.insert('1.0',h.nazwaH())
        o.insert('1.0',h.obraz())
        k.insert('1.0',h.osad())
        t.pack()
        o.pack()
        k.pack()
    okno=Tkinter.Tk()
    h=Hexagram()
    okno.wm_title('IChing - GJ2012')
    t=Tkinter.Text(okno,height=5)
    o=Tkinter.Text(okno,height=10)
    k=Tkinter.Text(okno,height=10)
    b=Tkinter.Button(okno,text="Generuj nowy heksagram!", command=gener) 
##    t.insert('1.0',h.nazwaH())
##    o.insert('1.0',h.obraz())
##    k.insert('1.0',h.osad())
###Iching-hexagram-01.png
##    t.pack()
##    o.pack()
##    k.pack()
    b.pack()
    okno.mainloop()

#testuj(1)
testujGUI()
