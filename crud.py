from neo4j import GraphDatabase
import json, datetime

# Importando as configurações no arquivo JSON
config = json.loads(open('config.json').read())
username = config["username"]
password = config["password"]

# Conexão com o Neo4j
class Neo4jCRUD:
    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()

    # CREATE
    def create_person(self, name, age):
        with self.driver.session() as session:
            session.run("CREATE (p:Person {name: $name, age: $age}) RETURN p", name=name, age=age)

    # READ
    def get_person(self, name):
        with self.driver.session() as session:
            result = session.run("MATCH (p:Person {name: $name}) RETURN p.name AS name, p.age AS age", name=name)
            return [record for record in result]

    # UPDATE
    def update_person_age(self, name, age):
        with self.driver.session() as session:
            session.run("MATCH (p:Person {name: $name}) SET p.age = $age RETURN p", name=name, age=age)

    # DELETE
    def delete_person(self, name):
        with self.driver.session() as session:
            session.run("MATCH (p:Person {name: $name}) DELETE p", name=name)


if __name__ == "__main__":
    uri = "bolt://localhost:7687"  # URL do Neo4j

    db = Neo4jCRUD(uri, username, password)

    # CREATE
    db.create_person("Alice", 30)
    db.create_person("Bob", 24)

    # READ
    people = db.get_person("Alice")
    print("Pessoa encontrada:", people)

    # UPDATE
    db.update_person_age("Alice", 31)

    # DELETE
    db.delete_person("Bob")

    db.close()