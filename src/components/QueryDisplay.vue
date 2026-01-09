<script setup>
import {defineModel} from "vue";

const props = defineProps({
    query: { type: String },
    isLoading: { type: Boolean },
    searchEngineName: { type: String },
});

const emit = defineEmits(['search', 'copy']);

const engineModel = defineModel('engine');

const searchEngines = {
    google: { name: "Google" },
    duckduckgo: { name: "DuckDuckGo" },
    bing: { name: "Bing" },
    yahoo: { name: "Yahoo" },
    brave: { name: "Brave" },
};
</script>

<template>
        <div class="card">
        <h3 class="section-title">Moteur de Recherche</h3>
        <select v-model="engineModel" class="input-field">
            <option v-for="(engine, key) in searchEngines" :key="key" :value="key">
                {{ engine.name }}
            </option>
        </select>
        <div class="query-header">
            <h2 class="query-title">Requête générée ({{ searchEngineName }})</h2>
            <div class="query-actions">
                <button
                    @click="emit('copy')"
                    type="button"
                    class="btn btn-component"
                    title="Copier la requête"
                >
                    Copier
                </button>
                <button
                    @click="emit('search')"
                    :disabled="isLoading"
                    type="button"
                    class="btn btn-component"
                >
                    <span v-if="isLoading" class="loader"></span>
                    {{ isLoading ? 'Recherche en cours...' : 'Lancer la Recherche' }}
                </button>
            </div>
        </div>

        <div class="query-preview">
            <p :class="['query-text', { 'query-text-placeholder': !query }]">
                {{ query || 'La requête sera générée ici' }}
            </p>
        </div>
    </div>
</template>