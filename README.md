# Jenkins-python-demo

Tämä projekti on esimerkki modernista CI/CD-työnkulusta (Continuous Integration). Olen rakentanut Python-sovelluksen, jonka laadunvarmistus on automatisoitu Jenkinsillä.

## 📸 Jenkins toiminnassa

Ohessa kuvakaappauksia rakentamastani automaatiosta.

### 1. Build History & Automaatio
Jenkins tarkkailee GitHub-repositoriota (Poll SCM). Alla näkyy historia ajetuista testeistä.

<img width="757" height="396" alt="all-tests" src="https://github.com/user-attachments/assets/486c204b-0f4a-4515-8c6c-f87b8cdd6358" />


### 2. Onnistunut suoritus (Green Pipeline)
Kun koodi on kunnossa, putki etenee vaiheittain:
1. **Setup:** Virtuaaliympäristön luonti ja riippuvuuksien asennus.
2. **Linting:** Koodin tyylin tarkistus (`flake8`), joka varmistaa PEP 8 -standardin.
3. **Test:** Yksikkötestien ajo (`pytest`) ja raportointi.

<img width="757" height="396" alt="passed-tests" src="https://github.com/user-attachments/assets/a137863b-4f7e-4ed3-b1d5-4870b1bb8281" />


### 3. Virheiden kiinniotto (Quality Gate)
Simuloin tilanteen, jossa koodiin päätyi bugi. Jenkins havaitsi virheen testeissä ja pysäytti putken välittömästi (punainen status). Tämä estää virheellisen version etenemisen.

<img width="757" height="396" alt="failed-tests" src="https://github.com/user-attachments/assets/b988d011-3f1d-4673-ac6d-506e20dcf4bd" />


## 🚀 Miten se toimii?
Joka kerta kun koodia päivitetään GitHubiin, Jenkins:
1. **Hakee** uusimman version koodista.
2. **Luo** eristetyn virtuaaliympäristön (Python venv).
3. **Asentaa** riippuvuudet automaattisesti.
4. **Suorittaa** yksikkötestit (`pytest`) ja mittaa testikattavuuden (`pytest-cov`).
5. **Raportoi** tulokset visuaalisesti Jenkinsin käyttöliittymään.

## 🛠 Teknologiat
* **Python 3:** Sovelluslogiikka ja tyyppiturvallisuus.
* **Pytest:** Kattava yksikkötestaus (100% code coverage).
* **Jenkins:** CI-automaatio ja Pipeline-skriptaus (Groovy).
* **Docker:** Jenkins-palvelimen ja build-ympäristön hallinta.
* **Git:** Versionhallinta.

## 📊 Testausstrategia
Testit kattavat:
* Peruslaskutoimitukset.
* Virhetilanteet (esim. nollalla jakaminen).
* Tyyppitarkistukset (TypeError väärillä syötteillä).
* Liukulukujen tarkkuuden (`approx`).

---
*Projekti on luotu työnhaun portfolio-työksi osoittamaan DevOps- ja Python-osaamista.*
