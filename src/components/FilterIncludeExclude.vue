<script setup>
import { defineModel } from 'vue';

const includeWords = defineModel('includeWords');
const excludeWords = defineModel('excludeWords');
const groupedTerms = defineModel('groupedTerms');
</script>

<template>
    <div class="card">
        <h3 class="section-title">Inclusions & Exclusions</h3>
        <div class="form-group">
            <label>Inclure les mots <span class="label-info">(+mot)</span></label>
            <input type="text" v-model="includeWords" placeholder="Séparez par des virgules: mot1, mot2" class="input-field" />
        </div>
        <div class="form-group">
            <label>Exclure les mots <span class="label-info">(-mot)</span></label>
            <input type="text" v-model="excludeWords" placeholder="Séparez par des virgules: mot1, mot2" class="input-field" />
        </div>
        <div class="form-group">
            <label>Termes groupés <span class="label-info">((mot1 mot2))</span></label>
            <input type="text" v-model="groupedTerms" placeholder="Ex: guide débutant" class="input-field" />
        </div>
    </div>
</template>