function ajouterConfigUtil() {

    console.log("ajouter une config");

    reset();
    document.getElementById("id_materiel").innerHTML = "Une configuration complète :\n" +

        "\t1 Ordinateur portable avec processeurs I3- HP ou DELL avec écran 15 pouces/SSD 128 GO minimum/8 GO de RAM/Windows Pro/de préférence avec Prise RG45 sinon un DOC\n" +
        "\t1 clavier\n" +
        "\t1 souris\n" +
        "\t2 écrans 24 pouces IIYAMA\n" +
        "\t1 adaptateur carte vidéo externe (s’il y a qu’une prise HDMI sur le PC)";
}

function reset() {
    console.log("reset !");
    document.getElementById("id_materiel").innerHTML = "";
}

function afficherCommentaire(id) {

    $("#commentaireId_" + id).toggle("slow");
}