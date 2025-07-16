import logging

def generate_invitations(template, attendees):
    """
    Generates personalized invitation files from a template and list of attendees.
    
    Args:
        template (str): The template string with placeholders
        attendees (list): List of dictionaries containing attendee data
        
    Returns:
        None: Creates output files or logs errors
    """
    
    # Set up logging
    logging.basicConfig(level=logging.INFO)
    
    # Check input types
    if not isinstance(template, str):
        logging.error("Invalid input type: template must be a string")
        return
        
    if not isinstance(attendees, list) or not all(isinstance(x, dict) for x in attendees):
        logging.error("Invalid input type: attendees must be a list of dictionaries")
        return
    
    # Check for empty template
    if not template.strip():
        logging.error("Template is empty, no output files generated.")
        return
    
    # Check for empty attendees list
    if not attendees:
        logging.info("No data provided, no output files generated.")
        return
    
    # Process each attendee
    for i, attendee in enumerate(attendees, start=1):
        # Create a copy of the template for each attendee
        invitation = template
        
        # Replace each placeholder with the attendee's data or 'N/A' if missing
        for key in ['name', 'event_title', 'event_date', 'event_location']:
            value = attendee.get(key, 'N/A')
            if value is None:  # Handle explicit None values
                value = 'N/A'
            invitation = invitation.replace(f'{{{key}}}', str(value))
        
        # Write to output file
        filename = f'output_{i}.txt'
        try:
            with open(filename, 'w') as f:
                f.write(invitation)
            logging.info(f"Successfully created {filename}")
        except IOError as e:
            logging.error(f"Failed to write {filename}: {str(e)}")
