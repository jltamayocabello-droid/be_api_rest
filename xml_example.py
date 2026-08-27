from fastapi import FastAPI
from fastapi.responses import Response

app = FastAPI()

@app.get("/user-xml")
def get_user_xm ():
    xml_content = """
    <user>
        <id>19</id>
        <name>Guillermo Beltran</name>
        <active>True</active>
    </user>
    """
    return Response(
        content=xml_content, 
        media_type="application/xml"
    )