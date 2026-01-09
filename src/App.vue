<script setup>
import {ref, computed} from 'vue';
import SearchTerms from './components/SearchTerms.vue';
import FilterIncludeExclude from './components/FilterIncludeExclude.vue';
import FilterContent from './components/FilterContent.vue';
import FilterPeriodLocation from './components/FilterPeriodLocation.vue';
import FilterSpecialOperators from './components/FilterSpecialOperators.vue';
import QuickHelp from './components/QuickHelp.vue';
import QueryDisplay from './components/QueryDisplay.vue';
import SearchHistory from './components/SearchHistory.vue';

// Global states
const currentPage = ref('main');
const searchEngine = ref('google');
const searchTerms = ref([{value: '', type: 'normal'}]);
const operator = ref('AND');
const includeWords = ref('');
const excludeWords = ref('');
const groupedTerms = ref('');
const fileType = ref('');
const customFileType = ref('');
const site = ref('');
const inTitle = ref('');
const inUrl = ref('');
const inText = ref('');
const source = ref('');
const dateRange = ref('');
const related = ref('');
const location = ref('');
const define = ref('');
const weather = ref('');
const stocks = ref('');
const map = ref('');
const movie = ref('');

const isLoading = ref(false);

const searchEngines = {
    google: {name: "Google", url: "https://www.google.com/search?q="},
    duckduckgo: {name: "DuckDuckGo", url: "https://duckduckgo.com/?q="},
    bing: {name: "Bing", url: "https://www.bing.com/search?q="},
    yahoo: {name: "Yahoo", url: "https://search.yahoo.com/search?p="},
    brave: {name: "Brave", url: "https://search.brave.com/search?q="},
};

// Requête générée
const generatedQuery = computed(() => {
    let query = "";

    const validTerms = searchTerms.value.filter(term => term.value.trim());
    if (validTerms.length > 0) {
        let termsList = [];
        for (let term of validTerms) {
            if (term.type === "exact") {
                termsList.push(`"${term.value}"`);
            } else {
                termsList.push(`${term.value}`);
            }
        }
        query += termsList.join(` ${operator.value} `);
        if (termsList.length > 1){
            query = `(${query})`;
        }
    }

    // Filtres
    const fileTypeValue = fileType.value === "autre" ? customFileType.value : fileType.value;
    if (fileTypeValue) query += ` filetype:${fileTypeValue}`;
    if (site.value) query += ` site:${site.value}`;
    if (inTitle.value) query += ` intitle:${inTitle.value}`;
    if (inUrl.value) query += ` inurl:${inUrl.value}`;
    if (inText.value) query += ` intext:${inText.value}`;

    // Inclusions/Exclusions
    if (excludeWords.value) {
        excludeWords.value.split(',').map(w => w.trim()).forEach(w => w && (query += ` -${w}`));
    }
    if (includeWords.value) {
        includeWords.value.split(',').map(w => w.trim()).forEach(w => w && (query += ` +${w}`));
    }
    if (groupedTerms.value) query += ` (${groupedTerms.value})`;

    // Période/Localisation
    if (dateRange.value) query += ` ${dateRange.value}`;
    if (related.value) query += ` related:${related.value}`;
    if (location.value) query += ` location:${location.value}`;

    // Opérateurs Spéciaux
    if (define.value) query += ` define:${define.value}`;
    if (weather.value) query += ` weather:${weather.value}`;
    if (stocks.value) query += ` stocks:${stocks.value}`;
    if (map.value) query += ` map:${map.value}`;
    if (movie.value) query += ` movie:${movie.value}`;
    if (source.value) query += ` source:${source.value}`;

    return query.trim();
});

const currentEngineName = computed(() => {
    return searchEngines[searchEngine.value].name
});

const handleCopy = () => {
    const query = generatedQuery.value;
    if (query) {
        // Aide IA: How to copy text to clipboard in js
        navigator.clipboard.writeText(query);
        alert("Requête copiée dans le presse-papiers!");
    }
};

const handleSearch = () => {
    const query = generatedQuery.value;
    if (query) {
        // Aide IA: Best way to save this data in local storage in js
        // Logique de sauvegarde dans l'historique
        const historyEntry = {
            query,
            timestamp: Date.now(),
            searchEngine: currentEngineName.value,
            parameters: {
                searchTerms: searchTerms.value.filter(t => t.value.trim()).map(t => ({value: t.value, type: t.type})),
                fileType: fileType.value === "autre" ? customFileType.value : fileType.value,
                site: site.value, inTitle: inTitle.value, inUrl: inUrl.value, inText: inText.value,
                excludeWords: excludeWords.value, includeWords: includeWords.value, operator: operator.value,
                dateRange: dateRange.value, related: related.value, location: location.value,
                groupedTerms: groupedTerms.value, define: define.value, weather: weather.value,
                stocks: stocks.value, map: map.value, movie: movie.value, source: source.value
            }
        };

        const savedHistory = localStorage.getItem("searchHistory");
        const history = savedHistory ? JSON.parse(savedHistory) : [];
        history.unshift(historyEntry);
        if (history.length > 50) history.pop();
        localStorage.setItem("searchHistory", JSON.stringify(history));

        window.open(`${searchEngines[searchEngine.value].url}${encodeURIComponent(query)}`, '_blank');
    } else {
        alert("Veuillez entrer au moins un terme de recherche");
    }
};

// Aide IA: How to load localstorage params on my app
const handleLoadQuery = (entry) => {
    const params = entry.parameters;

    searchTerms.value = (params.searchTerms || []).map((t) => ({
        value: t.value,
        type: t.type
    }));
    if (searchTerms.value.length === 0) {
        searchTerms.value = [{value: '', type: 'normal'}];
    }

    fileType.value = params.fileType;
    site.value = params.site;
    inTitle.value = params.inTitle;
    inUrl.value = params.inUrl;
    inText.value = params.inText;
    excludeWords.value = params.excludeWords;
    includeWords.value = params.includeWords;
    operator.value = params.operator;
    dateRange.value = params.dateRange;
    related.value = params.related;
    location.value = params.location;
    groupedTerms.value = params.groupedTerms;
    define.value = params.define;
    weather.value = params.weather;
    stocks.value = params.stocks;
    map.value = params.map;
    movie.value = params.movie;
    source.value = params.source;

    // Retour à la vue principale
    setCurrentPage("main");
    // alert("Recherche chargée depuis l'historique");
};

const setCurrentPage = (page) => {
    currentPage.value = page
}

</script>

<template>
    <div class="app-container">
        <div v-if="currentPage === 'main'" class="main-view">

            <div class="header-section">
                <h1 class="main-title">Recherche Avancée</h1>
                <button @click="currentPage = 'history'" type="button" class="btn btn-app">
                    Historique
                </button>
            </div>

            <QueryDisplay
                v-model:engine="searchEngine"
                :query="generatedQuery"
                :is-loading="isLoading"
                :search-engine-name="currentEngineName"
                @search="handleSearch"
                @copy="handleCopy"
            />

            <div class="filter-grid">
                <div class="col-main">
                    <SearchTerms
                        v-model:terms="searchTerms"
                        v-model:operator="operator"
                    />


                    <FilterIncludeExclude
                        v-model:include-words="includeWords"
                        v-model:exclude-words="excludeWords"
                        v-model:grouped-terms="groupedTerms"
                    />

                    <FilterPeriodLocation
                        v-model:date-range="dateRange"
                        v-model:location="location"
                        v-model:related="related"
                    />
                </div>

                <div class="col-sidebar">
                    <FilterContent
                        v-model:file-type="fileType"
                        v-model:custom-file-type="customFileType"
                        v-model:site="site"
                        v-model:in-title="inTitle"
                        v-model:in-url="inUrl"
                        v-model:in-text="inText"
                    />

                    <FilterSpecialOperators
                        v-model:define="define"
                        v-model:weather="weather"
                        v-model:stocks="stocks"
                        v-model:map="map"
                        v-model:movie="movie"
                        v-model:source="source"
                    />

                    <QuickHelp/>
                </div>
            </div>

        </div>

        <div v-else-if="currentPage === 'history'">
            <SearchHistory
                @back="currentPage = 'main'"
                @load-query="handleLoadQuery"
            />
        </div>
    </div>
</template>