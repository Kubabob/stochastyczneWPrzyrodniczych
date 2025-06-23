# English version

## Stochastic Processes in Natural Sciences

This repository contains implementations of various stochastic processes and models commonly used in natural sciences, including percolation theory, random walks, and population genetics models.

### Installation and Configuration

#### Clone the Repository
```bash
git clone https://github.com/Kubabob/stochastic-models-in-science.git
cd stochastic-models-in-science
```

#### Installing Dependencies with uv
[uv](https://github.com/astral-sh/uv) is a fast Python package installer written in Rust, offering significantly better performance than pip.

1. Install uv (if not already installed):
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

2. Create a virtual environment and install dependencies:
```bash
uv venv
source .venv/bin/activate  # On Linux/macOS
# or
# .venv\Scripts\activate  # On Windows

# Install required packages
uv sync
```

#### Alternative Installation with pip
If you don't use uv, you can install dependencies using standard pip:

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Linux/macOS
# or
# venv\Scripts\activate  # On Windows
```

2. Install required packages:
```bash
pip install numpy matplotlib seaborn jupyter scipy pandas
```

### Content

#### Percolation Problem (`przenikanie.ipynb`)

A comprehensive Jupyter notebook implementing the classic percolation problem - a fundamental issue in statistical physics modeling flow through random porous media.

**Features:**

- Efficient grid generation with adjustable percolation probability
- Dynamic path-finding algorithm using depth-first search with memoization
- Statistical analysis of percolation probability vs. cell opening probability
- Visualization of phase transitions for different grid sizes
- Determination of critical thresholds at which phase transitions occur

The implementation demonstrates the critical phenomenon of percolation theory, showing how the system undergoes a sharp phase transition at a critical probability threshold (approximately 0.59 for a square grid).

#### Random Walk Simulations (`spacer-losowy.py`)

A Python module implementing random walk models in 1D, 2D, and 3D spaces with comprehensive analysis tools.

**Features:**

- Configurable random walk simulations in multiple dimensions
- Visualization tools for single and multiple random walks
- Statistical analysis including expected values and return probabilities
- Interactive 3D visualization with rotation capability
- Generation of histograms for position distributions

The implementation allows analysis of fundamental properties of random walks, such as the probability of returning to origin and expected distribution of final position.

#### Moran Model (`moran_model.ipynb`)

A Jupyter notebook implementing the Moran model - a stochastic process used in population genetics to model the dynamics of finite populations with selection.

**Features:**

- Configurable parameters for population size, mutation rate, and fitness advantage
- Interactive visualization of population evolution over time
- Parallel processing capabilities for multiple simulations
- Statistical analysis of fixation probabilities
- Animation of population frequency changes

The notebook demonstrates how selection and genetic drift affect the probability of fixation and extinction in finite populations.

#### Chemical Reactions (`reakcje.py`)

A module designed for simulating the dynamics of chemical reactions using stochastic approaches.

### Technologies Used

- Python 3
- NumPy for numerical operations
- Matplotlib and Seaborn for data visualization
- Multiprocessing for parallel simulations
- Jupyter Notebooks for interactive analysis

### Applications

These implementations can be used for:

- Educational purposes to understand fundamental stochastic processes
- Research in statistical physics, biology, and applied mathematics
- Modeling physical systems with random components
- Simulating population dynamics in evolutionary biology

Each implementation contains detailed documentation and examples showing how to use and extend the code for specific applications.

# Polska wersja

## Procesy Stochastyczne w Naukach Przyrodniczych

Repozytorium zawiera implementacje różnych procesów stochastycznych i modeli powszechnie stosowanych w naukach przyrodniczych, w tym teorii perkolacji, błądzenia losowego oraz modeli genetyki populacyjnej.

### Instalacja i konfiguracja

#### Pobieranie repozytorium
```bash
git clone https://github.com/Kubabob/stochastic-models-in-science.git
cd stochastic-models-in-science
```

#### Instalacja zależności za pomocą uv
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

#### Alternatywna instalacja za pomocą pip
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

### Zawartość

#### Problem Przenikania (`przenikanie.ipynb`)

Kompleksowy notebook Jupyter implementujący klasyczny problem perkolacji - fundamentalne zagadnienie fizyki statystycznej modelujące przepływ przez losowe ośrodki porowate.

**Funkcje:**

- Efektywne generowanie siatki z regulowanym prawdopodobieństwem perkolacji
- Dynamiczny algorytm znajdowania ścieżek wykorzystujący przeszukiwanie wgłąb z memoizacją
- Analiza statystyczna prawdopodobieństwa perkolacji względem prawdopodobieństwa otwarcia komórki
- Wizualizacja przejść fazowych dla różnych rozmiarów siatki
- Określanie progów krytycznych, przy których zachodzą przejścia fazowe

Implementacja demonstruje krytyczne zjawisko teorii perkolacji, pokazując jak system przechodzi przez ostre przejście fazowe przy krytycznym progu prawdopodobieństwa (około 0,59 dla siatki kwadratowej).

#### Symulacje Błądzenia Losowego (`spacer-losowy.py`)

Moduł Python implementujący modele błądzenia losowego w przestrzeniach 1D, 2D i 3D z kompleksowymi narzędziami analizy.

**Funkcje:**

- Konfigurowalne symulacje błądzenia losowego w wielu wymiarach
- Narzędzia wizualizacji dla pojedynczych i wielokrotnych błądzeń losowych
- Analiza statystyczna obejmująca wartości oczekiwane i prawdopodobieństwa powrotu
- Interaktywna wizualizacja 3D z możliwością rotacji
- Generowanie histogramów dla rozkładów pozycji

Implementacja pozwala na analizę fundamentalnych właściwości błądzenia losowego, takich jak prawdopodobieństwo powrotu do początku oraz oczekiwany rozkład końcowej pozycji.

#### Model Morana (`moran_model.ipynb`)

Notebook Jupyter implementujący model Morana - proces stochastyczny stosowany w genetyce populacyjnej do modelowania dynamiki skończonych populacji z selekcją.

**Funkcje:**

- Konfigurowalne parametry rozmiaru populacji, współczynnika mutacji i przewagi fitness
- Interaktywna wizualizacja ewolucji populacji w czasie
- Możliwości przetwarzania równoległego dla wielu symulacji
- Analiza statystyczna prawdopodobieństw utrwalenia
- Animacja zmian częstości populacji

Notebook demonstruje, jak selekcja i dryf genetyczny wpływają na prawdopodobieństwo utrwalenia i wyginięcia w skończonych populacjach.

#### Reakcje Chemiczne (`reakcje.py`)


Moduł przeznaczony do symulowania dynamiki reakcji chemicznych przy użyciu podejść stochastycznych.

### Wykorzystane Technologie

- Python 3
- NumPy do operacji numerycznych
- Matplotlib i Seaborn do wizualizacji danych
- Multiprocessing do symulacji równoległych
- Jupyter Notebooks do interaktywnej analizy

### Zastosowania

Te implementacje mogą być wykorzystane do:

- Celów edukacyjnych dla zrozumienia fundamentalnych procesów stochastycznych
- Badań w fizyce statystycznej, biologii i matematyce stosowanej
- Modelowania systemów fizycznych z losowymi komponentami
- Symulowania dynamiki populacji w biologii ewolucyjnej

Każda implementacja zawiera szczegółową dokumentację i przykłady pokazujące, jak używać i rozszerzać kod dla konkretnych zastosowań.