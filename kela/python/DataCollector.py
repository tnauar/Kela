import random
from datetime import date, timedelta
from RandomData import RandomData

class DataCollector():

    def __init__(self):
        pass

    def choose_visit_portal_digital(self) -> str:
        """Chooses randomly the digital visit portal.
        
        Args:
            None.
            
        Returns: A string that contains the digital visit portal and sometimes "Err".
        """
        portal_dig = random.choice(RandomData.VISIT_PORTAL_DIGITAL)
        planted_error = random.choices(["no", "yes"], k=1, weights=[0.99, 0.01])[0]
        if planted_error == "yes":
            return "Err"
        return portal_dig

    def choose_visit_portal_personal(self) -> str:
        """Chooses randomly the personal visit portal.
        
        Args:
            None.
            
        Returns: A string that contains the personal visit portal and sometimes "null".
        """
        portal_per = random.choice(RandomData.VISIT_PORTAL_PERSONAL)
        planted_error = random.choices(["no", "yes"], k=1, weights=[0.99, 0.01])[0]
        if planted_error == "yes":
            return "null"
        return portal_per

    def choose_service_event(self) -> str:
        """Generates a random service event.
        
        Args:
            None.
            
        Returns: A string that contains a random service event and sometimes " " character.
        """
        event = random.choice(RandomData.SERVICE_EVENT)
        planted_error = random.choices(["no", "yes"], k=1, weights=[0.99, 0.01])[0]
        if planted_error == "yes":
            return " "
        return event

    def choose_behaviour(self) -> str:
        """Generates a random behaviour description.
        
        Args:
            None.
            
        Returns: A string that contains a behaviour.
        """
        beh = random.choice(RandomData.BEHAVIOUR)
        return beh

    def choose_attitude(self) -> str:
        """Generates a random attitude description.
        
        Args:
            None.
            
        Returns: A string that contains an attitude.
        """

        att = random.choice(RandomData.ATTITUDE)
        return att

    def choose_functionality(self) -> str:
        """Generates a random functionality description.
        
        Args:
            None.
            
        Returns: A string that contains a functionality description.
        """
        func = random.choice(RandomData.FUNCTIONALITY)
        return func

    def choose_service_experience(self) -> str:
        """Generates a random number between 0-10 for the service experience. 
        It is weighted in the typical values.
        
        Args:
            None.
            
        Returns: A number for service experience.
        """
        values = list(range(11))
        weights = [1, 1, 1, 1, 2, 3, 5, 10, 5, 2, 1]

        se_number = random.choices(values, weights=weights, k=1)[0]

        return se_number

    def free_text_gen(self, portal_type: str, portal: str, event: str, beh: str, att: str, func: str)-> str:
        """Generates a free text field using templates and the arguments given to it.
        
        Args:
            portal_type: A string describing which portal is used: digital or personal.
            portal: A string describing the actual portal.
            event: A string describing the event.
            beh: A string describing the behaviour.
            att: A string describing the attitude.
            func: A string describing the functionality.
            
        Returns: A string that contains a template filled with given describing arguments.
        """

        if  portal_type == "portal_dig":
            template = random.choice(RandomData.TEMPLATES_DIGITAL_CHANNEL_EVAL)
            return template.format(
            portal_dig=portal,
            func=func,
            event=event
        )
        else:
            template = random.choice(RandomData.TEMPLATES_SERVICE_EVAL)
            return template.format(
            portal_per=portal,
            func=func,
            event=event,
            att=att,
            beh=beh
        )


    def collect_data(self) -> list[dict]:
        """Creates 10000 dicts from the random values and collects them to a list. 
        Each data file type has different random values and
        different amount of columns and the columns are in a different order.
        The main point is that the data files content is different so that we can use SQL to set them in a same format.
        
        Args:
            filetype: A string that defines the schema of the file. Different values are csv, json, parquet, xlsx.
            
        Returns: A list containing dicts that each contain one row of random data.
        """

        rows = []

        for i in range(1, 10000):

            person_id = random.randint(1, 5000)
            event = self.choose_service_event()
            beh = self.choose_behaviour()
            att = self.choose_attitude()
            func = self.choose_functionality()
            portal_type = random.choices(["portal_dig", "portal_per"], weights=[0.8, 0.2], k=1)[0]

            if portal_type == "portal_dig":
                portal = self.choose_visit_portal_digital()
            else:
                portal = self.choose_visit_portal_personal()

            
            
            se_number = self.choose_service_experience()
            free_text = self.free_text_gen(portal_type, portal, event, beh, att, func)


            row = {
                "rivi_nro": i,
                "henkilö_id": person_id,
                "käynnin_tyyppi": event,
                "palvelukanava": portal,
                "palvelukokemus": se_number,
                "palauteteksti": free_text
            }
            rows.append(row)       
        return rows
