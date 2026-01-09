<script setup>
const operators = [
    {op: 'filetype:', desc: 'Type de fichier (PDF, DOCX, etc.)'},
    {op: 'site:', desc: 'Recherche limitée à un site'},
    {op: 'intitle:', desc: 'Mots dans le titre de la page'},
    {op: 'inurl:', desc: 'Mots dans l\'URL de la page'},
    {op: 'intext:', desc: 'Mots dans le texte de la page'},
    {op: 'related:', desc: 'Pages similaires à une URL'},
    {op: 'location:', desc: 'Résultats liés à un lieu'},
    {op: 'define:', desc: 'Définir un mot'},
    {op: 'weather:', desc: 'Météo'},
    {op: 'stocks:', desc: 'Actions boursières'},
    {op: 'map:', desc: 'Carte'},
    {op: 'movie:', desc: 'Film'},
    {op: 'source:', desc: 'Source d\'actualités'},
];
</script>

<template>
    <div class="card">
        <h3 class="section-title">Aide Rapide (Opérateurs)</h3>
        <ul class="operator-list">
            <li v-for="op in operators" :key="op.op">
                <span class="operator-name">{{ op.op }}</span>
                <span class="operator-description">{{ op.desc }}</span>
            </li>
        </ul>
    </div>
</template>