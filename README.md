# 🎬 Filmlista és Statisztikai Mikroszerviz

**Készítette:** [A TE NEVED]  
**Intézmény:** Eszterházy Károly Katolikus Egyetem  
**Kurzus:** Multi paradigmás programozási nyelvek gyakorlat  
**Neptun kód:** [A TE NEPTUN KÓDOD]

---

## 📝 Projekt leírása
Ez az alkalmazás egy modern, mikroszerviz-architektúrájú projekt, amely Python nyelven készült. A célja egy személyes filmnapló vezetése, ahol a felhasználó rögzítheti a megnézett filmjeit, azok műfaját, és automatikus statisztikát kaphat a gyűjteményéről.

## 🛠️ Alkalmazott technológiák és paradigmák
A projekt megfelel a kurzus minden technikai előírásának:
* **Backend:** FastAPI keretrendszer REST API végpontokkal.
* **Frontend:** Streamlit alapú webes felület vizualizációval.
* **Adatbázis:** SQLite tartós tárolás SQLAlchemy ORM használatával.
* **Paradigmák:** * **Objektumorientált (OOP):** Adatbázis modellek (osztályok) használata.
    * **Funkcionális:** List comprehension és típusos adatszerkezetek.
    * **Procedurális:** Logikai folyamatok strukturált függvényekben.
* **Automatizáció:** BeautifulSoup alapú web scraping modul (külső adatok ellenőrzése).
* **Tesztelés:** Pytest egységtesztek @pytest.mark.parametrize dekorátorral.

## 🚀 Telepítés és futtatás
1.  **Virtuális környezet létrehozása és aktiválása:**
    ```powershell
    python -m venv venv
    .\venv\Scripts\activate
    ```
2.  **Függőségek telepítése:**
    ```powershell
    pip install -r requirements.txt
    ```
3.  **Backend indítása:**
    ```powershell
    uvicorn backend.main:app --reload
    ```
4.  **Frontend indítása:**
    ```powershell
    streamlit run frontend/app.py
    ```

## 🧪 Tesztelés futtatása
Az automatizált tesztek lefuttatásához használd a következő parancsot az aktív virtuális környezetben:
```powershell
pytest

Online elérhetőségek
GitHub Repository: [https://github.com/aknaaa1/MPNY]

Backend (Render): [IDE A RENDER LINKED]

Frontend (Streamlit Cloud): [IDE A STREAMLIT LINKED]
