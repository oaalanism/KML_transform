import psycopg2
import simplekml
try:
    connection = psycopg2.connect(user="postgres",
                                  password="explain",
                                  host="laflowbox.explainconsultancy.com",
                                  port="5432",
                                  database="laflowbox")
    cursor = connection.cursor()
    postgreSQL_select_Query = 'SELECT * FROM "OPENTOUR".trajectory ORDER BY trajectory_id'

    cursor.execute(postgreSQL_select_Query)
    print("Selecting rows from mobile table using cursor.fetchall")
    mobile_records = cursor.fetchall()

    kml = simplekml.Kml(name="OpenTour Line ")

    ls = kml.newlinestring(name = "line")

    coords = []
    for row in mobile_records:
        coords.append([row[3], row[2]])
    ls.coords = coords
    ls.style.linestyle.color = simplekml.Color.rgb(54, 103, 227)
    kml.save("./KML/OpenTour.kml")
except (Exception, psycopg2.Error) as error:
    print("Error while fetching data from PostgreSQL", error)