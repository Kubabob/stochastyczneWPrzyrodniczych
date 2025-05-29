# Procesy Stochastyczne w Naukach Przyrodniczych

Repozytorium zawiera implementacje różnych procesów stochastycznych i modeli powszechnie stosowanych w naukach przyrodniczych, w tym teorii perkolacji, błądzenia losowego oraz modeli genetyki populacyjnej.

## Instalacja i konfiguracja

### Pobieranie repozytorium
```bash
git clone https://github.com/username/stochastyczneWPrzyrodniczych.git
cd stochastyczneWPrzyrodniczych
```

### Instalacja zależności za pomocą uv
[uv](https://github.com/astral-sh/uv) to szybki instalator pakietów Python napisany w Rust, oferujący znacznie lepszą wydajność niż pip.

1. Instalacja uv (jeśli jeszcze nie zainstalowano):
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

2. Tworzenie środowiska wirtualnego i instalacja zależności:
```bash
uv venv
source .venv/bin/activate  # Na Linuxie/macOS
# lub
# .venv\Scripts\activate  # Na Windows

# Instalacja wymaganych pakietów
uv sync
```

### Alternatywna instalacja za pomocą pip
Jeżeli nie korzystasz z uv, możesz zainstalować zależności przy użyciu standardowego pip:

1. Tworzenie środowiska wirtualnego:
```bash
python -m venv venv
source venv/bin/activate  # Na Linuxie/macOS
# lub
# venv\Scripts\activate  # Na Windows
```

2. Instalacja wymaganych pakietów:
```bash
pip install numpy matplotlib seaborn jupyter scipy pandas
```

## Zawartość

### Problem Przenikania (`przenikanie.ipynb`)

Kompleksowy notebook Jupyter implementujący klasyczny problem perkolacji - fundamentalne zagadnienie fizyki statystycznej modelujące przepływ przez losowe ośrodki porowate.

**Funkcje:**

- Efektywne generowanie siatki z regulowanym prawdopodobieństwem perkolacji
- Dynamiczny algorytm znajdowania ścieżek wykorzystujący przeszukiwanie wgłąb z memoizacją
- Analiza statystyczna prawdopodobieństwa perkolacji względem prawdopodobieństwa otwarcia komórki
- Wizualizacja przejść fazowych dla różnych rozmiarów siatki
- Określanie progów krytycznych, przy których zachodzą przejścia fazowe

Implementacja demonstruje krytyczne zjawisko teorii perkolacji, pokazując jak system przechodzi przez ostre przejście fazowe przy krytycznym progu prawdopodobieństwa (około 0,59 dla siatki kwadratowej).

### Symulacje Błądzenia Losowego (`spacer-losowy.py`)

Moduł Python implementujący modele błądzenia losowego w przestrzeniach 1D, 2D i 3D z kompleksowymi narzędziami analizy.

**Funkcje:**

- Konfigurowalne symulacje błądzenia losowego w wielu wymiarach
- Narzędzia wizualizacji dla pojedynczych i wielokrotnych błądzeń losowych
- Analiza statystyczna obejmująca wartości oczekiwane i prawdopodobieństwa powrotu
- Interaktywna wizualizacja 3D z możliwością rotacji
- Generowanie histogramów dla rozkładów pozycji

Implementacja pozwala na analizę fundamentalnych właściwości błądzenia losowego, takich jak prawdopodobieństwo powrotu do początku oraz oczekiwany rozkład końcowej pozycji.

### Model Morana (`moran_model.ipynb`)

Notebook Jupyter implementujący model Morana - proces stochastyczny stosowany w genetyce populacyjnej do modelowania dynamiki skończonych populacji z selekcją.

**Funkcje:**

- Konfigurowalne parametry rozmiaru populacji, współczynnika mutacji i przewagi fitness
- Interaktywna wizualizacja ewolucji populacji w czasie
- Możliwości przetwarzania równoległego dla wielu symulacji
- Analiza statystyczna prawdopodobieństw utrwalenia
- Animacja zmian częstości populacji

Notebook demonstruje, jak selekcja i dryf genetyczny wpływają na prawdopodobieństwo utrwalenia i wyginięcia w skończonych populacjach.

### Reakcje Chemiczne (`reakcje.py`)

<!-- > **Uwaga:** Ten moduł jest obecnie w fazie rozwoju. -->

Moduł przeznaczony do symulowania dynamiki reakcji chemicznych przy użyciu podejść stochastycznych.

## Wykorzystane Technologie

- Python 3
- NumPy do operacji numerycznych
- Matplotlib i Seaborn do wizualizacji danych
- Multiprocessing do symulacji równoległych
- Jupyter Notebooks do interaktywnej analizy

## Zastosowania

Te implementacje mogą być wykorzystane do:

- Celów edukacyjnych dla zrozumienia fundamentalnych procesów stochastycznych
- Badań w fizyce statystycznej, biologii i matematyce stosowanej
- Modelowania systemów fizycznych z losowymi komponentami
- Symulowania dynamiki populacji w biologii ewolucyjnej

Każda implementacja zawiera szczegółową dokumentację i przykłady pokazujące, jak używać i rozszerzać kod dla konkretnych zastosowań.