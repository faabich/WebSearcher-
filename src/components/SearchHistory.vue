<script setup>
import {ref, defineEmits, onMounted} from 'vue';

const emit = defineEmits(['back', 'load-query']);

const history = ref([]);

onMounted(() => {
    const savedHistory = JSON.parse(localStorage.getItem('searchHistory'))
    for (let historyEntry of savedHistory) {
        history.value.push(historyEntry);
    }
})

const handleDeleteEntry = (timestamp) => {
    history.value = history.value.filter(entry => entry.timestamp !== timestamp);
    localStorage.setItem('searchHistory', JSON.stringify(history.value));
};

const handleClearHistory = () => {
    history.value = [];
    localStorage.removeItem('searchHistory');
};

const handleCopyQuery = (query) => {
    navigator.clipboard.writeText(query);
    alert('Requête copiée !');
};

const handleLoadQuery = (entry) => {
    emit('load-query', entry);
};

</script>

<template>
    <div>
        <div class="header-section">
            <h2 class="main-title">
                Historique de Recherche
            </h2>
            <button
                @click="emit('back')"
                type="button"
                class="btn btn-app"
            >
                Retour
            </button>
        </div>

        <div v-if="history.length === 0" class="card">
            <p class="query-text-placeholder">Aucune recherche enregistrée.</p>
        </div>

        <div v-else>
            <div class="header-group">
                <span></span>
                <button
                    @click="handleClearHistory"
                    class="btn btn-red"
                >
                    Effacer tout
                </button>
            </div>

            <div class="col-main">
                <div v-for="entry in history" :key="entry.timestamp" class="card history-item">
                    <div>
                        <div>
                            <p class="query-text">{{ entry.query }}</p>

                            <div class="history-metadata">
                                <span class="label-info">
                                    Search made the {{
                                        new Date(entry.timestamp).toLocaleString()
                                    }} on {{ entry.searchEngine }}
                                </span>
                            </div>
                        </div>

                        <div class="query-actions">
                            <button
                                @click="handleCopyQuery(entry.query)"
                                title="Copier la requête"
                                class="btn btn-component"
                            >
                                Copier
                            </button>
                            <button
                                @click="handleLoadQuery(entry)"
                                title="Charger cette recherche"
                                class="btn btn-component"
                            >
                                Charger
                            </button>
                            <button
                                @click="handleDeleteEntry(entry.timestamp)"
                                title="Supprimer"
                                class="btn btn-red"
                            >
                                Supprimer
                            </button>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>