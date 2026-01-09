<script setup>
import { defineModel } from 'vue';

const define = defineModel('define');
const weather = defineModel('weather');
const stocks = defineModel('stocks');
const map = defineModel('map');
const movie = defineModel('movie');
const source = defineModel('source');
</script>

<template>
    <div class="card filter-section">
        <h3 class="section-title">Opérateurs Spéciaux</h3>
        <div class="form-grid">
            <div class="form-group">
                <label>Définition <span class="label-info">(define:)</span></label>
                <input type="text" v-model="define" placeholder="Mot à définir" class="input-field" />
            </div>
            <div class="form-group">
                <label>Météo <span class="label-info">(weather:)</span></label>
                <input type="text" v-model="weather" placeholder="Lieu" class="input-field" />
            </div>
            <div class="form-group">
                <label>Actions <span class="label-info">(stocks:)</span></label>
                <input type="text" v-model="stocks" placeholder="Symbole (ex: AAPL)" class="input-field" />
            </div>
            <div class="form-group">
                <label>Carte <span class="label-info">(map:)</span></label>
                <input type="text" v-model="map" placeholder="Adresse ou lieu" class="input-field" />
            </div>
            <div class="form-group">
                <label>Film <span class="label-info">(movie:)</span></label>
                <input type="text" v-model="movie" placeholder="Titre du film" class="input-field" />
            </div>
            <div class="form-group">
                <label>Source d'actualités <span class="label-info">(source:)</span></label>
                <input type="text" v-model="source" placeholder="Nom de la source" class="input-field" />
            </div>
        </div>
    </div>
</template>