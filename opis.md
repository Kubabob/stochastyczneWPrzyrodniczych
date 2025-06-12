# Analiza Symulacji Reakcji Chemicznych

Plik `reakcje.ipynb` zawiera implementację różnych metod symulacji reakcji chemicznych przy użyciu podejść stochastycznych. Poniżej znajduje się opis przeprowadzonych symulacji oraz interpretacja uzyskanych wyników.

## Symulacja 1: Podstawowa Reakcja Rozpadu

Pierwsza symulacja implementuje prosty model stochastyczny reakcji rozpadu:


### Algorytm:
1. Ustalamy początkową liczbę cząsteczek A oraz stałą szybkości reakcji k
2. W każdym kroku symulacji:
   - Obliczamy prawdopodobieństwo zajścia reakcji jako A*k*dt
   - Losujemy liczbę z przedziału (0,1)
   - Jeśli wylosowana liczba jest mniejsza od obliczonego prawdopodobieństwa, to reakcja zachodzi (A zmniejsza się o 1)
   - Zwiększamy czas o dt

### Interpretacja wyników:
Wykres pokazuje wykładniczy spadek liczby cząsteczek A w czasie, co jest zgodne z oczekiwaniami dla reakcji pierwszego rzędu. Przy stałej szybkości k=0.1, obserwujemy charakterystyczny kształt krzywej, gdzie szybkość rozpadu jest proporcjonalna do liczby pozostałych cząsteczek. Im więcej cząsteczek pozostaje, tym szybciej przebiega reakcja, a wraz ze zmniejszaniem się ich liczby, proces zwalnia.

## Symulacja 2: Wielokrotne Powtórzenia i Uśrednianie

Druga część rozszerza pierwszą symulację, wykonując wiele powtórzeń (n=10) i obliczając średnią trajektorię.

### Algorytm:
1. Wykonujemy n niezależnych symulacji z tymi samymi parametrami
2. Wizualizujemy wszystkie trajektorie na jednym wykresie
3. Obliczamy i wyświetlamy średnią trajektorię

### Interpretacja wyników:
Wykres pokazuje znaczącą wariancję między poszczególnymi symulacjami, co odzwierciedla stochastyczną naturę procesu. Czerwona linia reprezentuje średnią z wszystkich symulacji, która przybliża deterministyczne rozwiązanie dla reakcji pierwszego rzędu. Jest to doskonała ilustracja, jak z wielu losowych procesów wyłania się przewidywalne zachowanie makroskopowe opisane równaniem różniczkowym.

## Symulacja 3: Reakcja z Tworzeniem i Rozpadem

Trzecia symulacja implementuje bardziej złożony model:


### Algorytm:
1. Obliczamy całkowitą intensywność reakcji (propensity) jako A*k + var*k
2. Czas do następnej reakcji jest losowany z rozkładu wykładniczego
3. Rodzaj reakcji (tworzenie lub rozpad) jest wybierany proporcjonalnie do ich intensywności
4. Odpowiednio aktualizujemy liczbę cząsteczek A

### Interpretacja wyników:
Ta symulacja pokazuje system, który osiąga stan równowagi dynamicznej, gdzie liczba cząsteczek fluktuuje wokół wartości równowagowej. Przy var=10 i k=0.1, system osiąga równowagę z około 10 cząsteczkami.

Gdy zwiększamy parametr var do 200, równowaga ustala się na wyższym poziomie (około 200 cząsteczek), co pokazuje, jak stosunek szybkości tworzenia do szybkości rozpadu determinuje stan równowagi.

Fluktuacje wokół wartości średniej ilustrują stochastyczną naturę procesów chemicznych na poziomie molekularnym, szczególnie widoczną w systemach z małą liczbą cząsteczek.

## Wnioski

Symulacje stochastyczne reakcji chemicznych pozwalają na modelowanie dynamiki procesów na poziomie pojedynczych cząsteczek, co jest niemożliwe przy użyciu podejścia deterministycznego (równań różniczkowych zwyczajnych). Są szczególnie wartościowe przy modelowaniu:

1. Systemów z małą liczbą cząsteczek, gdzie fluktuacje są znaczące
2. Procesów biologicznych, takich jak ekspresja genów czy enzymatyka
3. Reakcji chemicznych w ograniczonych przestrzeniach (np. pojedyncze komórki)

Przedstawione symulacje pokazują, jak z prostych reguł stochastycznych wyłaniają się makroskopowe wzorce zgodne z teorią kinetyki chemicznej, jednocześnie zachowując informacje o fluktuacjach nieobecnych w podejściu deterministycznym.

# Analiza Modelu Morana

Plik `moran_model.ipynb` zawiera implementację modelu Morana - procesu stochastycznego powszechnie stosowanego w genetyce populacyjnej do modelowania zmian częstości alleli w skończonych populacjach z uwzględnieniem selekcji i dryfu genetycznego.

## Teoria Modelu Morana

Model Morana jest dyskretnym procesem stochastycznym, który opisuje losowe zmiany częstości alleli w populacji o stałej wielkości. W każdym kroku czasowym:

1. Osobnik jest losowo wybierany do reprodukcji z prawdopodobieństwem proporcjonalnym do jego dostosowania (fitness)
2. Inny osobnik jest losowo wybierany do śmierci (z równym prawdopodobieństwem dla wszystkich)
3. Potomek pierwszego osobnika zastępuje osobnika, który umiera

Ten prosty model pozwala symulować kluczowe zjawiska ewolucyjne, takie jak dryf genetyczny i selekcja.

## Implementacja w Notebooku

### Podstawowa struktura

Notebook implementuje klasę `MoranModel` z następującymi parametrami:
- `population_size` - liczba osobników w populacji
- `mutation_rate` - współczynnik mutacji (prawdopodobieństwo zmiany typu potomka)
- `fitness_advantage` - przewaga dostosowawcza typu 1 nad typem 0

### Kluczowe metody

1. `step()` - wykonuje pojedynczy krok procesu Morana:
   - Wybiera osobnika do reprodukcji z prawdopodobieństwem zależnym od dostosowania
   - Wybiera losowego osobnika do śmierci
   - Zastępuje zmarłego osobnika potomkiem wybranym do reprodukcji

2. `run()` - uruchamia model przez określoną liczbę kroków i rejestruje historię zmian

3. `run_parallel_simulations()` - wykonuje wiele symulacji równolegle, wykorzystując wieloprocesowość

4. `visualize()` - tworzy interaktywną animację procesu

## Wyniki Symulacji

### Symulacja z przewagą selekcyjną

Pierwsza symulacja wykonuje model z parametrami:
- Populacja: 100 osobników
- Współczynnik mutacji: 0.001
- Przewaga dostosowawcza: 2.0

Symulacja rozpoczyna się od jednego mutanta (typu 1) i śledzi zmiany jego częstości w populacji. Wizualizacja pokazuje, jak częstość allelu zmienia się w czasie pod wpływem selekcji i dryfu genetycznego.

### Analiza wielu symulacji

Druga część notebooka wykonuje 1000 równoległych symulacji i analizuje prawdopodobieństwo utrwalenia (fixation):

- Populacja: 100 osobników
- Współczynnik mutacji: 0.001
- Przewaga dostosowawcza: 1.0 (neutralna ewolucja)
- Początkowa częstość mutanta: 50%

Wyniki pokazują:
1. Trajektorie pierwszych 20 symulacji - pokazujące różnorodność możliwych ścieżek ewolucyjnych
2. Średnią i medianę częstości w każdym punkcie czasowym
3. Przedział międzykwartylowy (25-75 percentyl)
4. Prawdopodobieństwo utrwalenia i wyginięcia

## Interpretacja Wyników

### Prawdopodobieństwo utrwalenia

W warunkach neutralnych (brak przewagi selekcyjnej), teoria przewiduje, że prawdopodobieństwo utrwalenia allelu jest równe jego początkowej częstości. Przy początkowej częstości 50%, oczekujemy prawdopodobieństwa utrwalenia około 0.5.

Wyniki symulacji potwierdzają to przewidywanie teoretyczne, co stanowi walidację poprawności implementacji modelu.

### Wpływ dryfu genetycznego

Symulacje wyraźnie pokazują wpływ dryfu genetycznego - losowych zmian częstości alleli wynikających z przypadkowego doboru do reprodukcji i śmierci. W małych populacjach (jak symulowane 100 osobników), dryf genetyczny może prowadzić do szybkiego utrwalenia lub wyginięcia allelu, nawet przy braku selekcji.

### Czas do utrwalenia

Analiza pokazuje również, że czas potrzebny do osiągnięcia utrwalenia lub wyginięcia może być bardzo zróżnicowany - niektóre populacje osiągają stan końcowy szybko, podczas gdy inne mogą utrzymywać pośrednie częstości przez długi czas.

## Wnioski

Model Morana dostarcza cennych informacji o dynamice małych populacji pod wpływem selekcji i dryfu genetycznego:

1. Nawet przy neutralnej ewolucji, populacja ostatecznie osiąga utrwalenie lub wyginięcie allelu
2. Prawdopodobieństwo utrwalenia bez selekcji jest równe początkowej częstości allelu
3. Dryf genetyczny ma silniejszy wpływ w małych populacjach
4. Selekcja może zwiększać lub zmniejszać prawdopodobieństwo utrwalenia, zależnie od kierunku

Model ten ma szerokie zastosowanie w badaniach ewolucyjnych, ekologii i genetyce populacyjnej, pomagając zrozumieć wpływ losowych procesów na ewolucję.

Implementacja w Pythonie z wykorzystaniem obliczeń równoległych pozwala na efektywne przeprowadzanie dużej liczby symulacji, co jest kluczowe dla uzyskania statystycznie istotnych wyników w procesach stochastycznych.

# Analiza Błądzenia Losowego

Plik `spacer-losowy.py` zawiera implementację symulacji błądzenia losowego (random walk) w przestrzeniach jedno-, dwu- i trójwymiarowych. Błądzenie losowe jest fundamentalnym procesem stochastycznym, który znajduje zastosowanie w fizyce, biologii, ekonomii oraz wielu innych dziedzinach nauki.

## Teoria Błądzenia Losowego

Błądzenie losowe to matematyczny model opisujący ścieżkę, która składa się z sekwencji losowych kroków. W najprostszej wersji jednowymiarowej:
- Cząsteczka rozpoczyna ruch w punkcie 0
- W każdym kroku cząsteczka przesuwa się o jedną jednostkę w lewo lub w prawo z równym prawdopodobieństwem (0.5)
- Proces jest całkowicie niezależny od poprzednich kroków (brak pamięci)

W wersjach wielowymiarowych, ruch odbywa się w losowo wybranym kierunku wzdłuż jednej z osi układu współrzędnych.

## Implementacja w Skrypcie

### Podstawowe funkcje generujące błądzenie

1. `spacer(ilosc_krokow)` - generuje jednowymiarowe błądzenie losowe
2. `spacer2D(ilosc_krokow)` - generuje dwuwymiarowe błądzenie losowe
3. `spacer3D(ilosc_krokow)` - generuje trójwymiarowe błądzenie losowe

Każda z tych funkcji zwraca listę zawierającą pozycje cząsteczki po każdym kroku.

### Funkcje do generowania wielu symulacji

1. `wiele_spacerow(ilosc_spacerow, ilosc_krokow)` - generuje wiele jednowymiarowych błądzeń
2. `wiele_spacerow2D(ilosc_spacerow, ilosc_krokow)` - generuje wiele dwuwymiarowych błądzeń
3. `wiele_spacerow3D(ilosc_spacerow, ilosc_krokow)` - generuje wiele trójwymiarowych błądzeń

### Funkcje wizualizacyjne

1. `pokaz_kroki(kroki)` - wyświetla wykres jednowymiarowego błądzenia
2. `pokaz_wiele_spacerow(lista_spacerow)` - wyświetla wiele jednowymiarowych błądzeń
3. `pokaz_wiele_spacerow2D(lista_spacerow)` - wyświetla wiele dwuwymiarowych błądzeń
4. `pokaz_wiele_spacerow3D(lista_spacerow)` - wyświetla wiele trójwymiarowych błądzeń w interaktywnym wykresie 3D

Szczególnie interesująca jest funkcja `pokaz_wiele_spacerow3D`, która tworzy interaktywną wizualizację umożliwiającą obracanie wykresu i obserwowanie trajektorii z różnych perspektyw.

### Funkcje analityczne

1. `wartosc_oczekiwana(lista_spacerow)` - oblicza średnią końcową pozycję dla wielu symulacji
2. `prawdopodobienstwo_bycia_w_miejscu(miejsce, lista_spacerow)` - oblicza prawdopodobieństwo znalezienia się w określonej pozycji
3. `histogram_wielu_spacerow(lista_spacerow)` - tworzy histogram końcowych pozycji
4. `prawdopodobienstwo_powrotu(lista_spacerow)` - oblicza prawdopodobieństwo powrotu do punktu początkowego

Te funkcje implementują kluczowe metody analizy statystycznej dla błądzenia losowego.

## Interpretacja Wyników

### Wartość oczekiwana pozycji

W symetrycznym błądzeniu losowym (z równym prawdopodobieństwem ruchu w każdym kierunku), wartość oczekiwana pozycji końcowej wynosi 0. Oznacza to, że średnio cząsteczka nie oddala się od punktu początkowego, mimo że indywidualne trajektorie mogą osiągać znaczne odległości.

### Prawdopodobieństwo powrotu

Jedno z najciekawszych zjawisk w teorii błądzenia losowego dotyczy prawdopodobieństwa powrotu do punktu początkowego:
- W przestrzeni 1D: prawdopodobieństwo powrotu wynosi 1 (cząsteczka zawsze wróci do początku)
- W przestrzeni 2D: prawdopodobieństwo powrotu wynosi 1 (cząsteczka zawsze wróci do początku)
- W przestrzeni 3D: prawdopodobieństwo powrotu jest mniejsze niż 1 (cząsteczka może nigdy nie wrócić)

Symulacje potwierdzają te teoretyczne wyniki, co stanowi fascynujący przykład, jak wymiarowość przestrzeni wpływa na fundamentalne właściwości procesów stochastycznych.

### Rozkład końcowych pozycji

Histogram końcowych pozycji dla dużej liczby symulacji pokazuje, że rozkład ten zbliża się do rozkładu normalnego (gaussowskiego). Jest to zgodne z centralnym twierdzeniem granicznym, ponieważ pozycja końcowa jest sumą wielu niezależnych losowych kroków.

## Zastosowania w Naukach Przyrodniczych

Błądzenie losowe znajduje liczne zastosowania w modelowaniu zjawisk przyrodniczych:

1. **Dyfuzja cząsteczek** - ruch Browna cząsteczek w płynie można modelować jako błądzenie losowe
2. **Migracja zwierząt** - wzorce przemieszczania się wielu gatunków zwierząt przypominają błądzenie losowe
3. **Rozprzestrzenianie się genów** - dryf genetyczny w populacjach można opisać za pomocą modeli błądzenia losowego
4. **Procesy transportu** - przemieszczanie się substancji w tkankach biologicznych często następuje przez dyfuzję
5. **Ewolucja molekularna** - zmiany w sekwencjach DNA mogą być modelowane jako błądzenie w przestrzeni sekwencji

Implementacja w tym skrypcie dostarcza narzędzi do badania tych zjawisk i analizowania ich statystycznych właściwości.

## Wnioski

Symulacje błądzenia losowego pokazują, jak proste reguły stochastyczne mogą prowadzić do złożonych i nieoczywistych zachowań. Pozwalają one zrozumieć fundamentalne własności procesów losowych, takie jak:

1. Rozkład pozycji w czasie
2. Prawdopodobieństwo powrotu do punktu początkowego
3. Średni kwadrat odległości (który rośnie liniowo z czasem)
4. Wpływ wymiarowości przestrzeni na zachowanie układu

Skrypt `spacer-losowy.py` stanowi wszechstronne narzędzie do badania tych właściwości, oferując zarówno funkcje symulacyjne, jak i analityczne, a także zaawansowane metody wizualizacji wyników.

# Analiza Problemu Przenikania

Plik `przenikanie.ipynb` zawiera implementację klasycznego problemu przenikania (perkolacji) - fundamentalnego zagadnienia z dziedziny fizyki statystycznej, które modeluje przepływ przez losowe ośrodki porowate.

## Teoria Problemu Przenikania

Problem przenikania można przedstawić za pomocą siatki kwadratowej, gdzie każda komórka jest losowo:
- Otwarta (przepuszczalna) z prawdopodobieństwem _p_
- Zamknięta (nieprzepuszczalna) z prawdopodobieństwem _1-p_

Kluczowe pytanie brzmi: dla jakiej wartości progowej prawdopodobieństwa _p_ istnieje ścieżka otwartych komórek łącząca górną i dolną krawędź siatki?

Zagadnienie to stanowi przykład zjawiska przejścia fazowego, gdzie układ drastycznie zmienia swoje właściwości przy niewielkiej zmianie parametru kontrolnego (w tym przypadku prawdopodobieństwa _p_).

## Implementacja w Notebooku

### Generowanie Siatki Perkolacyjnej

Notebook zaczyna od implementacji funkcji `stworz_tablice()`, która tworzy kwadratową siatkę NxN, gdzie każda komórka jest otwarta (wartość 1) lub zamknięta (wartość 0) zgodnie z zadanym prawdopodobieństwem _p_.

```python
def stworz_tablice(N: int, p: float) -> np.ndarray:
    tablica = np.random.random(size=(N,N))
    maska = tablica < p
    return maska.astype(int)
```

### Algorytm Wyszukiwania Ścieżki

Kluczową częścią implementacji jest algorytm sprawdzający, czy istnieje ścieżka perkolacyjna od górnej do dolnej krawędzi siatki. Wykorzystano tu przeszukiwanie wgłąb (DFS) z memoizacją:

1. `sprawdz_punkt()` - funkcja rekurencyjnie sprawdzająca, czy z danego punktu istnieje ścieżka do dolnej krawędzi
2. `sprawdz_tablice()` - funkcja sprawdzająca wszystkie możliwe punkty startowe w górnym wierszu

Dla optymalizacji wydajności zaimplementowano technikę programowania dynamicznego poprzez słownik `sprawdzone_punkty`, który zapobiega wielokrotnemu sprawdzaniu tych samych punktów.

### Symulacje i Analiza Statystyczna

Notebook zawiera funkcje do przeprowadzania symulacji perkolacji dla różnych wartości prawdopodobieństwa _p_ i rozmiarów siatki _N_:

1. `prawdopodobienstwo_przenikniecia()` - oblicza eksperymentalne prawdopodobieństwo perkolacji dla danego _p_ i _N_
2. `wyniki_dla_wszystkich_p()` - wykonuje symulacje dla zakresu wartości _p_ od 0 do 1
3. `pokaz_wyniki_dla_wszystkich_p_dla_kilku_N()` - porównuje wyniki dla różnych rozmiarów siatki

### Identyfikacja Punktu Krytycznego

Funkcja `punkt_krytyczny()` szacuje wartość progową _p_, przy której zachodzi przejście fazowe - jest to punkt, w którym prawdopodobieństwo perkolacji gwałtownie wzrasta z wartości bliskich 0 do wartości bliskich 1.

## Wyniki Symulacji

### Przejście Fazowe

Symulacje wyraźnie pokazują ostre przejście fazowe w okolicy _p_ ≈ 0.59 dla siatki o rozmiarze N=25. Jest to zbieżne z teoretyczną wartością 0.5927... dla nieskończonej siatki kwadratowej.

### Wpływ Rozmiaru Siatki

Notebook analizuje również, jak rozmiar siatki _N_ wpływa na charakter przejścia fazowego:

1. Dla małych siatek (N < 10) - przejście jest rozmyte, a punkt krytyczny mniej dokładny
2. Dla większych siatek (N > 20) - przejście staje się coraz bardziej ostre
3. Przy bardzo dużych siatkach (N > 100) - przejście praktycznie natychmiastowe

### Złożoność Obliczeniowa

W notebooku zwrócono uwagę na złożoność obliczeniową problemu:
- Czasowa: O(N²) dla generowania siatki + O(N⁴) dla algorytmu przeszukiwania w najgorszym przypadku
- Pamięciowa: O(N²)

Dzięki zastosowaniu programowania dynamicznego udało się znacząco zredukować czas obliczeń, umożliwiając symulacje nawet dla dużych siatek.

## Zastosowania Praktyczne

Problem perkolacji ma liczne zastosowania praktyczne:

1. **Modelowanie przepływu płynów** - badanie przepuszczalności ośrodków porowatych, np. złóż ropy naftowej
2. **Materiałoznawstwo** - analiza przewodnictwa elektrycznego w materiałach kompozytowych
3. **Epidemiologia** - modelowanie rozprzestrzeniania się chorób w populacjach
4. **Ekologia** - badanie rozprzestrzeniania się pożarów w lasach
5. **Nauki o materiałach** - projektowanie materiałów o określonej przepuszczalności

## Wnioski

Symulacje problemu perkolacji pokazują klasyczny przykład zjawiska krytycznego z wyraźnym przejściem fazowym. Punkt krytyczny _p_ ≈ 0.59 potwierdza teoretyczne przewidywania dla siatki kwadratowej.

Wraz ze wzrostem rozmiaru siatki przejście fazowe staje się coraz ostrzejsze, zbliżając się do idealnego przejścia dla nieskończonej siatki.

Implementacja z wykorzystaniem programowania dynamicznego pozwala na efektywne obliczenia nawet dla dużych siatek, co umożliwia dokładniejsze określenie właściwości przejścia fazowego.
