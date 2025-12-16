# 🌟 ADHD-Støtteapp

En digital støtteapp for personer med ADHD – laget for å redusere kognitiv belastning og gi hjelp med planlegging, gjennomføring og oversikt i hverdagen.

---

## 🧠 Hovedmål

- ✅ Redusere behovet for indre planlegging og husk
- ✅ Strukturere dagen med visuelle og enkle verktøy
- ✅ Skape mestring gjennom delmål og tilbakemelding
- ✅ Fjerne triggere: nøytrale farger, forutsigbar design
- ✅ Lett å bruke med én hånd – og enkle trykk

---

## 📱 Hovedfunksjoner (Screens)

| Funksjon              | Beskrivelse |
|-----------------------|-------------|
| 🏠 **HjemSkjerm**        | Minimalistisk oversikt med rolige farger og enkel navigasjon. Viser dagens viktigste oppgaver og påminnelser. |
| 🗓 **KalenderScreen.js** | Visuell kalender for å strukturere uken/dagen, synliggjør hva som er neste og hvor mye som gjenstår. |
| 📝 **ListerScreen.js**   | Egne lister for innkjøp, oppgaver, ideer – alt separert og fargekodet. Kan krysses av og slettes med ett trykk. |
| 🔄 **SmåOppgaverScreen.js** | "Små steg" – her kan brukeren bryte ned større oppgaver og få tilbakemelding ved å gjennomføre. |
| 🧱 **StoreOppgaverScreen.js** | Langsiktige oppgaver (f.eks. søknader, flytting) brytes ned i delmål med fremdrift. Viser progresjon og "Fullført". |
| ⚙️ **FullfortScreen.js**  | Oversikt over oppgaver og delmål som er gjort. Gir følelsen av mestring. |
| 🚿 **ADLScreen.js**       | Viser daglige rutiner (ADL = aktiviteter i dagliglivet) med tilpasning for energi og påminnelser. |

---

## 🛠 Teknisk stack

- **Frontend:** React Native / Expo (planlagt for Android og iOS)
- **Backend (valgfritt):** Firebase eller Node/Express med MongoDB eller SQLite
- **Push-varsler:** Expo Notifications
- **PWA-støtte:** Kan gjøres tilgjengelig via mobilens hjemskjerm

---

## 🧩 Struktur

\`\`\`
src/
├── screens/
│   ├── HomeScreen.js
│   ├── KalenderScreen.js
│   ├── ListerScreen.js
│   ├── SmaOppgaverScreen.js
│   ├── StoreOppgaverScreen.js
│   ├── FullfortScreen.js
│   └── ADLScreen.js
├── components/
│   ├── OppgaveKort.js
│   ├── KalenderVisning.js
│   └── ADLItem.js
├── assets/
│   └── icons/
├── App.js
└── app.json
\`\`\`

---

## 🔧 Utvikling og kjøring lokalt

1. Installer avhengigheter:
\`\`\`bash
npm install
\`\`\`

2. Start appen med Expo:
\`\`\`bash
npx expo start
\`\`\`

3. Scan QR-koden med Expo Go-appen på mobilen

---

## 🎯 Visuelt design

- Bruk av **dempede farger** (beige, lys grå, blågrønn)
- Store knapper og **ingen "overload"**
- Font: enkel sans-serif, minimum 16px
- Konsekvent ikonbruk og lydløs respons (valgfritt)

---

## 🚧 Planlagt utvikling

- [ ] Brukerprofil og tilpasning (farger, rutiner, nivå)
- [ ] Deling med veileder eller støtteperson
- [ ] Push-varslinger for ADL-oppgaver
- [ ] Offline-støtte
- [ ] AI-assistert forslag til plan

---

## ❤️ Hvem er appen for?

Denne appen er laget for:
- Personer med ADHD (eller ADD)
- Unge voksne i overgang til selvstendighet
- Voksne i jobb eller utdanning med behov for struktur

---

## 🧠 Inspirasjon

- [Wellbee](https://wellbee.no)
- [MemoAssist](https://memoassist.no)
- [Tody](https://todyapp.com)