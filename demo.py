from testcontainers.iris import IRISContainer
import sqlalchemy

iris_container = IRISContainer("intersystemsdc/iris-community:latest")
with iris_container as iris:
    engine = sqlalchemy.create_engine(iris.get_connection_url())
    with engine.begin() as connection:
        result = connection.execute(sqlalchemy.text("select $zversion"))
        version, = result.fetchone()
print(version)
