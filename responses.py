# responses.py
# Archivio di risposte per il chatbot vocale offline in italiano

import random

RESPONSES = {
    "saluti": [
        "Ciao! Come stai?",
        "Salve! Che piacere sentirti!",
        "Ehilà, come va?",
        "Buongiorno, spero tu abbia una splendida giornata!",
        "Ciao caro amico, pronto a chiacchierare?",
        "Ehi! Bentornato, mi sei mancato!",
        "Ciao, che novità ci sono oggi?",
        "Buonasera! Spero tu stia bene.",
        "Salve salve! Sono pronto ad ascoltarti.",
        "Ciao! È bello sentirti di nuovo.",
        "Ehilà! Tutto bene?",
        "Buongiorno! Hai fatto colazione?",
        "Ciao amico! Oggi sei di buon umore?",
        "Ciao! È una bella giornata per parlare.",
        "Bentornato! Raccontami qualcosa."
    ],
    "come_stai": [
        "Sto bene, grazie! E tu?",
        "Alla grande! Tu come te la passi?",
        "Un po' stanco ma felice di parlare con te.",
        "Oggi mi sento pieno di energia!",
        "Bene, bene! Tu invece?",
        "Sto molto meglio da quando ti sento.",
        "Non mi lamento, la vita va avanti!",
        "Felice e sereno, grazie a te.",
        "Non posso lamentarmi, ho la tua compagnia.",
        "Carico di curiosità per la nostra conversazione!"
    ],
    "nome": [
        "Mi chiamo Chatbot e sono qui per parlare con te.",
        "Puoi chiamarmi Assistente Virtuale.",
        "Sono il tuo compagno digitale di chiacchiere.",
        "Il mio nome non è importante, l'importante è che sono qui con te.",
        "Io sono il Chatbot offline più simpatico che tu abbia mai incontrato!",
        "Non ho un nome ufficiale, vuoi darmene uno tu?",
        "Sono una voce digitale, ma mi piace pensare di essere un amico.",
        "Il mio nome è... beh, facciamo che sia 'Chatbotino'.",
        "Puoi chiamarmi come preferisci!",
        "Sono il risultato di tante righe di codice, ma con tanta voglia di parlare."
    ],
    "tempo": [
        "Non lo so con precisione, ma spero sia una bella giornata!",
        "Il meteo non è il mio forte, ma secondo me c'è sempre il sole quando sorridi.",
        "Non ho accesso alle previsioni, ma posso dirti che oggi è un buon giorno.",
        "Se vuoi ti posso raccontare una poesia sul tempo... meteorologico o filosofico?",
        "Il tempo è relativo, diceva Einstein.",
        "Il meteo cambia, ma la tua energia resta!",
        "Sai che il tempo in Italia varia tantissimo da nord a sud?",
        "Pioggia o sole, l'importante è sorridere.",
        "Il tempo atmosferico non lo so, ma il tempo insieme è sempre bello.",
        "Per me oggi è sempre sereno, perché parlo con te."
    ],
    "barzellette": [
        "Sai qual è il colmo per un elettricista? Non capire la corrente.",
        "Perché il computer è andato dal dottore? Perché aveva un virus!",
        "Sai cosa fa un pomodoro timido? Diventa rosso.",
        "Qual è l'animale più antico? La zebra, perché è in bianco e nero!",
        "Cosa fa un libro in palestra? Solleva capitoli!",
        "Sai perché i fantasmi non mentono? Perché sono trasparenti!",
        "Che fa una mucca in palestra? Latte in polvere!",
        "Sai qual è il colmo per un ladro? Rubare il tempo agli altri.",
        "Sai cosa dice un cane all'altro? 'Bau, ci vediamo dopo!'",
        "Perché la gallina attraversa la strada? Per andare dall'altra parte!"
    ],
    "curiosita": [
        "Lo sapevi che le api possono riconoscere i volti umani?",
        "Un polpo ha tre cuori.",
        "Gli squali esistono da prima degli alberi.",
        "Lo sapevi che il cuore di una balena blu può pesare fino a 200 chili?",
        "In Giappone ci sono più animali domestici che bambini.",
        "Le lumache possono dormire fino a tre anni.",
        "La lingua della giraffa può essere lunga fino a 50 centimetri.",
        "Le stelle marine possono rigenerare le braccia perdute.",
        "Gli elefanti sono gli unici animali che non possono saltare.",
        "Il miele non va mai a male, nemmeno dopo migliaia di anni."
    ],
    "motivazione": [
        "Credi sempre in te stesso, sei più forte di quanto pensi.",
        "Ogni giorno è una nuova opportunità per migliorarti.",
        "Non arrenderti, le cose belle richiedono tempo.",
        "Ricorda: anche i piccoli passi portano lontano.",
        "Il successo è la somma di piccoli sforzi ripetuti giorno dopo giorno.",
        "Non mollare mai: chi persevera raggiunge la meta.",
        "I tuoi sogni meritano di essere inseguiti.",
        "Ogni ostacolo è un'opportunità di crescita.",
        "Il futuro appartiene a chi crede nella bellezza dei propri sogni.",
        "Vai avanti, anche quando è difficile: la forza è dentro di te."
    ],
    "proverbi": [
        "Chi dorme non piglia pesci.",
        "Ride bene chi ride ultimo.",
        "Meglio soli che male accompagnati.",
        "Chi la dura la vince.",
        "Non tutto il male vien per nuocere.",
        "L'erba del vicino è sempre più verde.",
        "Tra il dire e il fare c'è di mezzo il mare.",
        "Chi trova un amico trova un tesoro.",
        "A caval donato non si guarda in bocca.",
        "Tanto va la gatta al lardo che ci lascia lo zampino."
    ],
    "indovinelli": [
        "Sono sempre davanti a te, ma non puoi mai vedermi. Chi sono? — Il futuro.",
        "Più me ne togli, più divento grande. Chi sono? — Una buca.",
        "Ho le gambe ma non cammino. Chi sono? — Un tavolo.",
        "Sono pieno di buchi ma contengo l'acqua. Chi sono? — Una spugna.",
        "Volo senza ali e piango senza occhi. Chi sono? — La nuvola.",
        "Ho una sola voce ma faccio eco a mille. Chi sono? — L'eco.",
        "Più mi lavi e più divento sporco. Chi sono? — L'acqua.",
        "Se mi nomini, scompaio. Chi sono? — Il silenzio.",
        "Entro duro ed esco molle. Chi sono? — Lo spaghetto cotto.",
        "Se mi rompi non faccio male. Chi sono? — Un uovo."
    ],
    "uscita": [
        "Arrivederci, alla prossima!",
        "Ciao, è stato bello parlare con te!",
        "Alla prossima chiacchierata!",
        "Ti saluto con un sorriso virtuale!",
        "Addio, ma solo per ora!"
    ],
    "default": [
        "Non ho ancora una risposta a questa domanda.",
        "Interessante! Raccontami di più.",
        "Mi dispiace, ma non so cosa rispondere.",
        "Potresti riformulare la domanda?",
        "Non capisco bene, vuoi ripetere?"
    ]
}

def get_response(category: str) -> str:
    if category in RESPONSES:
        return random.choice(RESPONSES[category])
    return random.choice(RESPONSES["default"])
