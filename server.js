import express from 'express';
import bodyParser from "body-parser";
import cors from "cors"

const app = express();
const port = 3000;

// Middleware
app.use(cors());
app.use(bodyParser.json()); // Pour analyser le corps des requêtes JSON

// Endpoint de Recherche
app.post('/api/search', (req, res) => {
    const searchTerms = req.body.terms;
    const searchEngine = req.body.engine;

    if (!searchTerms || !Array.isArray(searchTerms)) {
        return res.status(400).json({ message: "Termes de recherche invalides." });
    }

    const queryParts = searchTerms
        .filter(term => term.value.trim() !== '')
        .map(term => term.type === 'exact' ? `"${term.value.trim()}"` : term.value.trim());

    const fullQuery = queryParts.join(' ');

    console.log(`--- Nouvelle Recherche sur ${searchEngine} ---`);
    console.log(`Requête générée: ${fullQuery}`);

    res.json({
        message: "Recherche enregistrée et traitée avec succès.",
        searchEngine: searchEngine,
        generatedQuery: fullQuery
    });
});

app.listen(port, () => {
    console.log(`Serveur Express en écoute sur http://localhost:${port}`);
});