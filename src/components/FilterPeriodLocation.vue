<script setup>
import {defineModel} from 'vue';

const dateRange = defineModel('dateRange');
const location = defineModel('location');
const related = defineModel('related');
</script>

<template>
    <div class="card">
        <h3 class="section-title">Période & Localisation</h3>
        <div class="form-grid">
            <div class="form-group form-group-full">
                <label>Période <span class="label-info">(dateRange)</span></label>
                <input type="text" v-model="dateRange" placeholder="Ex: after:2024-01-01" class="input-field"/>
            </div>
            <div class="form-group">
                <label>Localisation <span class="label-info">(location:)</span></label>
                <input type="text" v-model="location" placeholder="Ex: Paris" class="input-field"/>
            </div>
            <div class="form-group">
                <label>Pages liées <span class="label-info">(related:)</span></label>
                <input type="text" v-model="related" placeholder="Ex: example.com" class="input-field"/>
            </div>
        </div>
    </div>
</template>