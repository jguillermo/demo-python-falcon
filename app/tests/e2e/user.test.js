const request = require('@request');
const mysql = require('@mysql');

describe('Managament User', () => {

    test('Insert Ok', async () => {
        let {body, statusCode} = await request('/', 'POST', {name: 'jose',last_name: 'Guillermo'});
        expect(statusCode).toEqual(201);
        expect(body.data.id).toBeDefined();
        expect(body).toEqual(
            {"code": 2000,
                "data": {
                "id":body.data.id
                },
                "error": false,
                "message": "SUCCESS"
            });

        let results = await mysql(`SELECT name, last_name FROM user WHERE id = "${body.data.id}"`);
        expect(results[0].name).toEqual('jose');
        expect(results[0].last_name).toEqual('Guillermo');
    });

    test('Insert Error', async () => {
        let {body, statusCode} = await request('/', 'POST',{last_name:'Guillermo'});
        expect(statusCode).toEqual(500);
        expect(body).toEqual({
            "code": 4000,
            "data": [],
            "error": true,
            "message": "El nombre debe ser mayor a 2 caracteres"
        });
    });

    test('Update Error no existe le usuario', async () => {
        let {body, statusCode} = await request('/1', 'PUT', {name: 'jose'});
        expect(statusCode).toEqual(500);
        expect(body).toEqual({
                "code": 4000,
                "data": [],
                "error": true,
                "message": "No existe el usuario con id : 1"
            });
    });


    test('Update Error, no se envian todos los parametros', async () => {

        let {body:bodyInsert, statusCode:statusCodeInsert} = await request('/', 'POST', {name: 'jose',last_name: 'Guillermo'});
        id = bodyInsert.data.id;

        let {body, statusCode} = await request(`/${id}`, 'PUT',{names: 'jose'});
        expect(statusCode).toEqual(500);
        expect(body).toEqual({
            "code": 4000,
            "data": [],
            "error": true,
            "message":
                "El nombre debe ser mayor a 2 caracteres"
        });
    });

    test('Update Ok', async () => {
        let {body:bodyInsert, statusCode:statusCodeInsert} = await request('/', 'POST', {name: 'jose',last_name: 'Guillermo'});
        id = bodyInsert.data.id;

        let {body, statusCode} = await request(`/${id}`, 'PUT',{name: 'Antonio',last_name: 'Inche'});

        expect(body).toEqual({
            "code": 2000,
            "data": "ok",
            "error": false,
            "message": "SUCCESS"
        });
        expect(statusCode).toEqual(200);

        let results = await mysql(`SELECT name, last_name FROM user WHERE id = "${id}"`);
        expect(results[0].name).toEqual('Antonio');
        expect(results[0].last_name).toEqual('Inche');


    });

});


describe('List User', () => {
    test('listar un usuario que no existe', async () => {
        let {body, statusCode} = await request('/156');
        expect(statusCode).toEqual(500);
        expect(body).toEqual({
            "message": "No existe el usuario con id : 156",
            "code": 4000,
            "error": true,
            "data": []
        });
    });

    test('listar un usuario existe', async () => {

        let {body:bodyInsert, statusCode:statusCodeInsert} = await request('/', 'POST', {name: 'jose',last_name: 'Guillermo'});
        id = bodyInsert.data.id;

        let {body, statusCode} = await request(`/${id}`,'GET');
        expect(statusCode).toEqual(200);
        expect(body).toEqual({
            "code": 2000,
            "data": {
                "id": id,
                "last_name": "Guillermo",
                "name": "jose"
            },
            "error": false,
            "message": "SUCCESS"
        });
    });
});
