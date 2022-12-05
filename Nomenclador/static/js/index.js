const ListarRegion = async () => {
    try {
        const response = await fetch("./region")
        const data = await response.json();
        if (data.message === `Success`){
            let opciones = ``
            data.regiones.forEach((region) => {
                opciones+= `<option value="${region.id}">${region.nombre}</option>`
            })
            selectRegion.innerHTML = opciones;
            ListarProvincias(data.regiones[0].id)
        }
        else alert('Regiones no encontradas')
    }
    catch (error){
        console.log(error)
    }
}

const ListarProvincias = async (region) => {
    try {
        const response = await fetch(`./provincias/${region}`)
        const data = await response.json();
        if (data.message === 'Success'){
            let opciones = ``;
            data.provincias.forEach((provincia) => {
                opciones+= `<option value='${provincia.id}'>${provincia.nombre}</option>`
            })
            selectProvincia.innerHTML = opciones;
            ListarMunicipios(data.provincias[0].id)
        }
        else alert('Provincias no encontradas')

    }
    catch (error){
        console.log(error)
    }
}

const ListarMunicipios = async (provincia) => {
    try {
        const response = await fetch(`./municipios/${provincia}`)
        const data = await response.json();
        if (data.message === 'Success'){
            let opciones = ``;
            data.municipios.forEach((municipio) => {
                opciones+= `<option value='${municipio.id}'>${municipio.nombre}</option>`
            })
            selectMunicipio.innerHTML = opciones;
        }
        else alert('Municipios no encontrados')

    }
    catch (error){
        console.log(error)
    }
}

const CargaInicial = async () => {
    await ListarRegion();
    selectRegion.addEventListener("change", (event) => {
        ListarProvincias(event.target.value)
    })
    selectProvincia.addEventListener("change", (event) => {
        ListarMunicipios(event.target.value)
    })

}

window.addEventListener("load", async () => {
    await CargaInicial();
})