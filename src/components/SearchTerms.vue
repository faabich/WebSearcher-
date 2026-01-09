<script setup>
import { defineModel} from 'vue';

const termsModel = defineModel('terms');
const operatorModel = defineModel('operator');

const addTerm = () => {
    termsModel.value.push({value: '', type: 'normal' });
};

const removeTerm = (value) => {
    if (termsModel.value.length > 1) {
        const index = termsModel.value.findIndex(term => term.value === value);
        termsModel.value.splice(index, 1);
    }
};

const toggleType = (value) => {
    const index = termsModel.value.findIndex(term => term.value === value);
    termsModel.value[index].type = termsModel.value[index].type === 'normal' ? 'exact' : 'normal';
};
</script>

<template>
    <div class="card">
        <div class="header-group section-title">
            <h3 class="title">Termes de Recherche</h3>
            <select v-model="operatorModel" class="input-field select-small">
                <option value="AND">AND (ET)</option>
                <option value="OR">OR (OU)</option>
            </select>
        </div>

        <div class="term-list">
            <div v-for="(term, index) in termsModel" :key="index" class="term-item">
                <input
                    v-model="termsModel[index].value"
                    type="text"
                    :placeholder="term.type === 'exact' ? 'Phrase exacte (ex: « pomme de terre »)' : 'Terme normal (ex: pomme)'"
                    class="input-field"
                />
                <button
                    @click="toggleType(term.value)"
                    type="button"
                    class="btn btn-component"
                    :title="term.type === 'exact' ? 'Basculer en normal' : 'Basculer en exact'"
                >
                    {{ term.type === 'exact' ? '" "' : 'Mot' }}
                </button>
                <button
                    v-if="termsModel.length > 1"
                    @click="removeTerm(term.value)"
                    type="button"
                    class="btn btn-red"
                    title="Supprimer le terme"
                >
                    X
                </button>
            </div>

            <button
                @click="addTerm"
                type="button"
                class="btn btn-component"
            >
                + Ajouter un terme
            </button>
        </div>
    </div>
</template>