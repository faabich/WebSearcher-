<script setup>
import {defineModel} from 'vue';

const fileType = defineModel('fileType');
const site = defineModel('site');
const inTitle = defineModel('inTitle');
const inUrl = defineModel('inUrl');
const inText = defineModel('inText');
</script>

<template>
    <div class="card">
        <h3 class="section-title">Filtres de Contenu</h3>
        <div class="form-grid">
            <div class="form-group">
                <label>Limiter au Site <span class="label-info">(site:)</span></label>
                <input type="text" v-model="site" placeholder="Ex: wikipedia.org" class="input-field"/>
            </div>
            <div class="form-group">
                <label>Dans le Titre <span class="label-info">(intitle:)</span></label>
                <input type="text" v-model="inTitle" placeholder="Ex: guide" class="input-field"/>
            </div>
            <div class="form-group">
                <label>Dans l'URL <span class="label-info">(inurl:)</span></label>
                <input type="text" v-model="inUrl" placeholder="Ex: faq" class="input-field"/>
            </div>
            <div class="form-group">
                <label>Dans le Texte <span class="label-info">(intext:)</span></label>
                <input type="text" v-model="inText" placeholder="Ex: recette" class="input-field"/>
            </div>
            <div class="form-group form-group-full">
                <label>Type de Fichier <span class="label-info">(filetype:)</span></label>
                <input type="text" v-model="fileType" placeholder="Ex: pdf" class="input-field"/>
            </div>
        </div>
    </div>
</template>