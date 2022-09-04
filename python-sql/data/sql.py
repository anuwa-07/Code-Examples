
# Define the class for SQL

import os
from tkinter import SW
from turtle import home
import aiomysql
from const import DATABASE_NAME, DATABASE_PASSWORD, DATABASE_POOL_SIZE, DATABASE_PORT, DATABASE_USERNAME, DATABSE_HOST





class SQL:

    def __init__(self) -> None:
        ''' No need to do anything here, We configure this class async support '''
        ...

    async def __aenter__(self):
        ''' __aenter__ is the strat point when we call on instance '''
        await self._initilize()
        return self
    
    async def __aexit__(self, exc_type, exc_value, traceback) -> None:
        ''' __aexit__ will trigger after every time end of the SQL conncetion '''
        self._connection_pool.close()
        await self._connection_pool.wait_closed()

    async def _initilize(self) -> None:
        """ creare the sql conncetion """
        self._connection_pool = await aiomysql.create_pool(
            host = DATABSE_HOST,
            port = DATABASE_PORT,
            user = DATABASE_USERNAME,
            password = DATABASE_PASSWORD,
            db = DATABASE_NAME,
            maxsize=DATABASE_POOL_SIZE,
            autocommit = True,
        )

    async def __execute_query(self, query:str, args:list=None):
        async with self._connection_pool.acquire() as conn :
            async with conn.cursor() as cur:
                await cur.execute(query, args)

    async def select(self, query, args=None, tag=None) :
        async with self._connection_pool.acquire() as conn :
            async with conn.cursor() as cur :
                await cur.execute(query, args)
                results = await cur.fetchall()
                if tag is None :
                    return results
                else :
                    return tag, results

    async def insert(self, query, args=None) :
        await self._execute_query(query, args)

    async def update(self, query, args=None) :
        await self._execute_query(query, args)

    async def check_connection(self) :
        async with self._connection_pool.acquire() as conn :
            async with conn.cursor() as cur :
                return True    

