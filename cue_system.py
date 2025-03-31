import os
import subprocess
import requests
import webbrowser
import smtplib
import paramiko
import git
import logging
from pptx import Presentation
from telegram import Bot

# Logger Configuration
logging.basicConfig(
    filename="cue_system.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class CUESystem:
    def __init__(self, env_file="Environment.txt", actions_file="ActionDetails.txt"):
        self.employees = self.load_environment(env_file)
        self.actions = self.load_actions(actions_file)
    
    def load_environment(self, filename):
        """Parse Environment.txt to extract employee details."""
        employees = []
        try:
            with open(filename, "r") as file:
                data = file.read().strip().split("\n\n")
                for block in data:
                    employee = {}
                    for line in block.split("\n"):
                        if ": " in line:
                            key, value = line.split(": ", 1)
                            employee[key.lower().replace(" ", "_")] = value
                    if employee:
                        employees.append(employee)
        except Exception as e:
            logging.error(f"Error loading environment: {e}")
        return employees
    
    def load_actions(self, filename):
        """Load the action details (for reference, not shown to the user)."""
        try:
            with open(filename, "r") as file:
                return file.read()
        except Exception as e:
            logging.error(f"Error loading actions: {e}")
            return ""
    
    # -------------------- Cybersecurity & Cryptographic Assessment Actions --------------------
    def crypto_scan(self):
        return "Cryptographic Discovery & Analysis executed (simulated)."
    
    def code_crypto_scan(self, source_directory):
        return f"Source code cryptography analysis on '{source_directory}' executed (simulated)."
    
    def net_scan(self, target_range):
        return f"Network security scanning on '{target_range}' executed (simulated)."
    
    def endpoint_assess(self, target_ip):
        return f"Endpoint security assessment on '{target_ip}' executed (simulated)."
    
    def validate_scan(self):
        return "Security post-scan validation executed (simulated)."
    
    def net_traffic_scan(self):
        return "Network traffic scanning (live & historical) executed (simulated)."
    
    def net_simulate(self, scenario):
        return f"Network simulation for scenario '{scenario}' executed (simulated)."
    
    def user_simulate(self, scenario):
        return f"User simulation for scenario '{scenario}' executed (simulated)."
    
    def human_activity_sim(self, attack_type):
        return f"Human activity simulation for attack type '{attack_type}' executed (simulated)."
    
    def network_testbed(self):
        return "Network testbed & sandboxing deployed (simulated)."
    
    def crypto_asset_manage(self):
        return "Cryptography asset management executed (simulated)."
    
    def key_exchange_test(self):
        return "Key exchange and secure communication test executed (simulated)."
    
    def pqc_eval(self):
        return "Quantum-safe & post-quantum cryptography evaluation executed (simulated)."
    
    def cicd_security_scan(self):
        return "CI/CD security integration scan executed (simulated)."
    
    def threat_hunt(self):
        return "Automated threat hunting executed (simulated)."
    
    # -------------------- RTC2 Function API (Ninja-Framework) --------------------
    def download_from_c2(self):
        return "Downloaded file from C2 to local host (simulated)."
    
    def upload_to_c2(self):
        return "Uploaded local file to C2 server (simulated)."
    
    # -------------------- Malware Task API (Ninja-Framework) --------------------
    def attack_run_command(self, command):
        return f"Attack Task: Command '{command}' executed on victim (simulated)."
    
    def attack_steal_file(self, file_path):
        return f"Attack Task: File '{file_path}' stolen from victim to C2-DB (simulated)."
    
    def attack_inject_file(self, file_path):
        return f"Attack Task: File '{file_path}' injected from C2-DB to victim (simulated)."
    
    def attack_capture_screenshot(self):
        return "Attack Task: Victim screenshot captured and uploaded to C2-DB (simulated)."
    
    def attack_ssh_command(self, ip, command):
        return f"Attack Task: SSH to victim {ip} executed command '{command}' (simulated)."
    
    def attack_scp_file(self, source, target):
        return "Attack Task: SCP file transfer from victim to target executed (simulated)."
    
    def attack_scan_subnet(self, subnet):
        return f"Attack Task: Sub-network scan of {subnet} executed (simulated)."
    
    def attack_key_event(self):
        return "Attack Task: Keyboard event generated on victim (simulated)."
    
    def attack_eavesdrop(self):
        return "Attack Task: Victim's traffic captured to pcap file (simulated)."
    
    def attack_add_special(self):
        return "Attack Task: Customized special action executed (simulated)."
    
    # -------------------- Communication Activities --------------------
    def send_telegram_message(self, bot_token, chat_id, message):
        """Send a message using Telegram bot."""
        try:
            bot = Bot(token=bot_token)
            bot.send_message(chat_id=chat_id, text=message)
            return f"Telegram message sent: {message}"
        except Exception as e:
            logging.error(f"Error sending Telegram message: {e}")
            return f"Failed to send Telegram message: {e}"
    
    # -------------------- Basic & Network Actions --------------------
    def ping_host(self, ip, parallel=False, show_console=False):
        """Ping targets (sequence or parallel)."""
        cmd = ["ping", "-n", "4", ip] if os.name == "nt" else ["ping", "-c", "4", ip]
        if not show_console:
            subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        else:
            subprocess.run(cmd)
        return f"Ping executed on {ip}."
    
    def capture_webpage_screenshot(self, url, save_path="screenshot.png"):
        logging.info(f"Capturing screenshot of {url} and saving to {save_path}.")
        return f"Screenshot of {url} saved to {save_path} (simulated)."
    
    def download_webpage(self, url, save_path="downloaded_page"):
        response = requests.get(url)
        if response.status_code == 200:
            os.makedirs(save_path, exist_ok=True)
            filepath = os.path.join(save_path, "index.html")
            with open(filepath, "w", encoding="utf-8") as file:
                file.write(response.text)
            return f"Webpage from {url} downloaded to {filepath}."
        return f"Failed to download webpage from {url}."
    
    def connect_ftp(self, ftp_server, username, password):
        logging.info(f"Connected to FTP server {ftp_server} as {username} (simulated).")
        return f"FTP connection to {ftp_server} established (simulated)."
    
    def connect_ssh(self, ip, username, password, command):
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(ip, username=username, password=password)
        stdin, stdout, stderr = client.exec_command(command)
        output = stdout.read().decode()
        client.close()
        return output
    
    def scp_file(self, source_path, target_ip, target_path, username, password):
        logging.info(f"SCP file from {source_path} to {target_ip}:{target_path} (simulated).")
        return f"SCP file from {source_path} to {target_ip}:{target_path} (simulated)."
    
    def ssh_port_forward(self, target_ip, local_port, remote_port, username, password):
        logging.info(f"SSH port forwarding from local {local_port} to {target_ip}:{remote_port} (simulated).")
        return f"SSH port forwarding from local {local_port} to {target_ip}:{remote_port} (simulated)."
    
    def udp_connect(self, target_ip, port):
        logging.info(f"UDP connection to {target_ip}:{port} (simulated).")
        return f"UDP connection to {target_ip}:{port} established (simulated)."
    
    def tcp_connect(self, target_ip, port):
        logging.info(f"TCP connection to {target_ip}:{port} (simulated).")
        return f"TCP connection to {target_ip}:{port} established (simulated)."
    
    def connect_sqlite3(self, db_path):
        import sqlite3
        try:
            conn = sqlite3.connect(db_path)
            conn.close()
            return f"Connected to SQLite3 database at {db_path}."
        except Exception as e:
            return f"Failed to connect to SQLite3 at {db_path}: {e}"
    
    def connect_influxdb(self, host, port, username, password, database):
        logging.info(f"Connected to InfluxDB at {host}:{port} (simulated).")
        return f"Connected to InfluxDB at {host}:{port} (simulated)."
    
    def send_email(self, sender_email, receiver_email, password, subject, body):
        message = f"Subject: {subject}\n\n{body}"
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message)
        return f"Email sent with subject '{subject}'."
    
    def open_url(self, url):
        webbrowser.open(url)
        return f"Opened URL: {url}."
    
    def connect_ntp(self, server):
        logging.info(f"Connected to NTP server {server} (simulated).")
        return f"Connected to NTP server {server} (simulated)."
    
    def send_http_request(self, url, method="GET", data=None):
        try:
            if method.upper() == "GET":
                response = requests.get(url)
            else:
                response = requests.post(url, data=data)
            return f"HTTP {method} to {url} returned status {response.status_code}."
        except Exception as e:
            return f"HTTP request failed: {e}"
    
    # -------------------- Application Activities --------------------
    def open_application(self, app_path):
        if os.name == "nt":
            os.startfile(app_path)
        else:
            subprocess.call(["open", app_path])
        return f"Application {app_path} started."
    
    def edit_powerpoint(self, ppt_path, text_to_add="Updated by CUESystem"):
        if os.path.exists(ppt_path):
            prs = Presentation(ppt_path)
            slide_layout = prs.slide_layouts[5]
            slide = prs.slides.add_slide(slide_layout)
            slide.shapes.title.text = text_to_add
            prs.save(ppt_path)
            return f"PowerPoint {ppt_path} edited."
        return f"PowerPoint file {ppt_path} not found."
    
    def start_zoom_meeting(self, meeting_link):
        return self.open_application(meeting_link)
    
    def clone_github_repo(self, repo_url, clone_path):
        git.Repo.clone_from(repo_url, clone_path)
        return f"Cloned repository {repo_url} into {clone_path}."
    
    def wireshark_capture(self, interface="eth0"):
        logging.info(f"Wireshark capture started on {interface} (simulated).")
        return f"Wireshark capture on {interface} started (simulated)."
    
    def ftk_imager_capture(self, target):
        logging.info(f"FTK Imager captured memory dump from {target} (simulated).")
        return f"Memory dump from {target} captured (simulated)."
    
    def connect_scheduler_plc(self, ip, command):
        logging.info(f"Command '{command}' sent to Scheduler PLC at {ip} (simulated).")
        return f"Scheduler PLC at {ip} executed command '{command}' (simulated)."
    
    def connect_siemens_rtu(self, ip, command):
        logging.info(f"Command '{command}' sent to Siemens RTU at {ip} (simulated).")
        return f"Siemens RTU at {ip} executed command '{command}' (simulated)."
    
    def nmap_scan(self, target):
        logging.info(f"Nmap scan on {target} initiated (simulated).")
        return f"Nmap scan on {target} completed (simulated)."
    
    def speed_test(self):
        logging.info("Network speed test executed (simulated).")
        return "Network speed: 100 Mbps (simulated)."
    
    # -------------------- Human Activities --------------------
    def record_user_actions(self):
        logging.info("User actions recorded (simulated).")
        return "User actions recorded (simulated)."
    
    def generate_keyboard_event(self):
        logging.info("Keyboard event generated (simulated).")
        return "Keyboard event generated (simulated)."
    
    def generate_mouse_event(self):
        logging.info("Mouse event generated (simulated).")
        return "Mouse event generated (simulated)."
    
    def start_chrome_dino(self):
        logging.info("Chrome started with Google Dino game (simulated).")
        return "Chrome started with Google Dino game (simulated)."
    
    def telegram_chat(self, message):
        return self.send_telegram_message("your_bot_token", "your_chat_id", message)
    
    def select_and_play_local_file(self, file_path):
        logging.info(f"Local file {file_path} opened (simulated).")
        return f"Local file {file_path} opened (simulated)."
    
    def connect_webcam(self):
        logging.info("Web camera connected and video captured (simulated).")
        return "Web camera video captured (simulated)."
    
    def play_sudoku(self):
        logging.info("Sudoku game started (simulated).")
        return "Sudoku game started (simulated)."
    
    # -------------------- System Activities --------------------
    def run_remote_command(self, ip, command):
        return self.run_system_command(command)
    
    def open_local_camera(self):
        logging.info("Local camera opened (simulated).")
        return "Local camera opened and video captured (simulated)."
    
    def rs232_comm(self, port, command):
        logging.info(f"RS232/485 command '{command}' executed on port {port} (simulated).")
        return f"RS232/485 command '{command}' executed on port {port} (simulated)."
    
    def check_os_state(self):
        state = os.uname() if hasattr(os, "uname") else "OS state info not available"
        logging.info("OS state checked.")
        return f"OS state: {state}"
    
    def ettercap_mirror(self, target):
        logging.info(f"Ettercap mirroring on {target} initiated (simulated).")
        return f"Ettercap mirroring on {target} executed (simulated)."
    
    def google_map_direction(self, destination):
        logging.info(f"Directions to {destination} fetched (simulated).")
        return f"Directions to {destination} (simulated)."
    
    def open_cytoscape(self, graph_file):
        logging.info(f"Cytoscape opened with {graph_file} (simulated).")
        return f"Cytoscape processed {graph_file} and converted graph to JSON (simulated)."
    
    def obfuscate_python(self, code):
        logging.info("Python code obfuscated (simulated).")
        return f"Obfuscated code: {code[::-1]} (simulated)."
    
    # -------------------- Additional FTP Action --------------------
    def ftp_connect(self, ftp_server, username, password):
        logging.info(f"Simulated FTP connection to {ftp_server} as {username}.")
        return f"FTP connection to {ftp_server} established (simulated)."
    
    # -------------------- Command Parsing & Interactive Execution --------------------
    def is_command(self, user_input):
        tokens = user_input.lower().split()
        # Check multi-token commands first
        multi_token_commands = [
            "edit ppt", "send email", "send telegram",
            "crypto_scan", "code_crypto_scan", "net_scan", "endpoint_assess",
            "validate_scan", "net_traffic_scan", "net_simulate", "user_simulate",
            "human_activity_sim", "network_testbed", "crypto_asset_manage",
            "key_exchange_test", "pqc_eval", "cicd_security_scan", "threat_hunt",
            "download_from_c2", "upload_to_c2",
            "attack_run", "attack_steal", "attack_inject", "attack_capture",
            "attack_ssh", "attack_scp", "attack_scan", "attack_keyevent", "attack_eavesdrop", "attack_special"
        ]
        if len(tokens) >= 2:
            two_token = tokens[0] + " " + tokens[1]
            if two_token in multi_token_commands:
                return True
        if tokens and tokens[0] in multi_token_commands:
            return True
        # Check single-token commands
        known_commands = [
            "ping", "screenshot", "download", "ftp", "ssh", "scp", "portforward",
            "udp", "tcp", "sqlite", "influx", "openurl", "ntp", "http", "startapp",
            "zoom", "git", "wireshark", "ftkimager", "plc", "rtu", "nmap", "speedtest",
            "record", "keyevent", "mouseevent", "chrome", "telegramchat", "playfile",
            "webcam", "sudoku", "remotecommand", "localcamera", "rs232", "osstate",
            "ettercap", "googlemap", "cytoscape", "obfuscate", "ftp_connect"
        ]
        return tokens and tokens[0] in known_commands

    def execute(self, user_input):
        tokens = user_input.split()
        if not tokens:
            return "No command provided."
        
        combined = " ".join(tokens[:2]).lower()
        if combined == "edit ppt":
            if len(tokens) < 3:
                ppt_path = input("Enter the PowerPoint file path: ")
                text_to_add = input("Enter the text to add/edit in the PowerPoint: ")
            else:
                ppt_path = tokens[2]
                if len(tokens) < 4:
                    text_to_add = input("Enter the text to add/edit in the PowerPoint: ")
                else:
                    text_to_add = " ".join(tokens[3:])
            return self.edit_powerpoint(ppt_path, text_to_add)
        
        if combined == "send email":
            default_password = os.getenv("EMAIL_PASSWORD", "")
            if len(tokens) < 5:
                sender = input("Enter sender email: ")
                receiver = input("Enter receiver email: ")
                subject = input("Enter email subject: ")
                body = input("Enter email message: ")
            else:
                sender = tokens[2]
                receiver = tokens[3]
                subject = tokens[4]
                body = " ".join(tokens[5:]) if len(tokens) > 5 else input("Enter email message: ")
            return self.send_email(sender, receiver, default_password, subject, body)
        
        if combined == "send telegram":
            if len(tokens) < 3:
                message = input("Enter Telegram message: ")
            else:
                message = " ".join(tokens[2:])
            return self.send_telegram_message("your_bot_token", "your_chat_id", message)
        
        cyber_commands = {
            "crypto_scan": self.crypto_scan,
            "code_crypto_scan": self.code_crypto_scan,
            "net_scan": self.net_scan,
            "endpoint_assess": self.endpoint_assess,
            "validate_scan": self.validate_scan,
            "net_traffic_scan": self.net_traffic_scan,
            "net_simulate": self.net_simulate,
            "user_simulate": self.user_simulate,
            "human_activity_sim": self.human_activity_sim,
            "network_testbed": self.network_testbed,
            "crypto_asset_manage": self.crypto_asset_manage,
            "key_exchange_test": self.key_exchange_test,
            "pqc_eval": self.pqc_eval,
            "cicd_security_scan": self.cicd_security_scan,
            "threat_hunt": self.threat_hunt,
            "download_from_c2": self.download_from_c2,
            "upload_to_c2": self.upload_to_c2,
            "attack_run": self.attack_run_command,
            "attack_steal": self.attack_steal_file,
            "attack_inject": self.attack_inject_file,
            "attack_capture": self.attack_capture_screenshot,
            "attack_ssh": self.attack_ssh_command,
            "attack_scp": self.attack_scp_file,
            "attack_scan": self.attack_scan_subnet,
            "attack_keyevent": self.attack_key_event,
            "attack_eavesdrop": self.attack_eavesdrop,
            "attack_special": self.attack_add_special
        }
        if tokens[0].lower() in cyber_commands:
            func = cyber_commands[tokens[0].lower()]
            if len(tokens) > 1:
                arg = tokens[1]
                return func(arg)
            else:
                return func()
        
        command = tokens[0].lower()
        args = tokens[1:]
        if command == "ping":
            ip = args[0] if args else "8.8.8.8"
            return self.ping_host(ip)
        elif command == "screenshot":
            url = args[0] if args else "http://example.com"
            return self.capture_webpage_screenshot(url)
        elif command == "download":
            url = args[0] if args else "http://example.com"
            return self.download_webpage(url)
        elif command == "ftp":
            ftp_server = args[0] if args else "ftp.example.com"
            username = args[1] if len(args) >= 2 else "anonymous"
            password = args[2] if len(args) >= 3 else ""
            return self.connect_ftp(ftp_server, username, password)
        elif command == "ssh":
            if len(args) >= 4:
                ip = args[0]
                username = args[1]
                password = args[2]
                ssh_command = " ".join(args[3:])
                return self.connect_ssh(ip, username, password, ssh_command)
            else:
                return "Insufficient parameters for SSH command."
        elif command == "scp":
            if len(args) >= 5:
                source_path = args[0]
                target_ip = args[1]
                target_path = args[2]
                username = args[3]
                password = args[4]
                return self.scp_file(source_path, target_ip, target_path, username, password)
            else:
                return "Insufficient parameters for SCP command."
        elif command == "portforward":
            if len(args) >= 5:
                target_ip = args[0]
                local_port = args[1]
                remote_port = args[2]
                username = args[3]
                password = args[4]
                return self.ssh_port_forward(target_ip, local_port, remote_port, username, password)
            else:
                return "Insufficient parameters for portforward command."
        elif command == "udp":
            target_ip = args[0] if args else "8.8.8.8"
            port = args[1] if len(args) >= 2 else "80"
            return self.udp_connect(target_ip, port)
        elif command == "tcp":
            target_ip = args[0] if args else "8.8.8.8"
            port = args[1] if len(args) >= 2 else "80"
            return self.tcp_connect(target_ip, port)
        elif command == "sqlite":
            db_path = args[0] if args else "database.db"
            return self.connect_sqlite3(db_path)
        elif command == "influx":
            host = args[0] if args else "localhost"
            port = args[1] if len(args) >= 2 else "8086"
            username = args[2] if len(args) >= 3 else ""
            password = args[3] if len(args) >= 4 else ""
            database = args[4] if len(args) >= 5 else "default"
            return self.connect_influxdb(host, port, username, password, database)
        elif command == "openurl":
            url = args[0] if args else "http://example.com"
            return self.open_url(url)
        elif command == "ntp":
            server = args[0] if args else "pool.ntp.org"
            return self.connect_ntp(server)
        elif command == "http":
            url = args[0] if args else "http://example.com"
            method = args[1] if len(args) >= 2 else "GET"
            data = " ".join(args[2:]) if len(args) >= 3 else None
            return self.send_http_request(url, method, data)
        elif command == "startapp":
            app_path = args[0] if args else ""
            return self.open_application(app_path)
        elif command == "zoom":
            meeting_link = args[0] if args else ""
            return self.start_zoom_meeting(meeting_link)
        elif command == "git":
            if len(args) >= 2:
                repo_url = args[0]
                clone_path = args[1]
                return self.clone_github_repo(repo_url, clone_path)
            else:
                return "Insufficient parameters for git command."
        elif command == "wireshark":
            interface = args[0] if args else "eth0"
            return self.wireshark_capture(interface)
        elif command == "ftkimager":
            target = args[0] if args else "target"
            return self.ftk_imager_capture(target)
        elif command == "plc":
            ip = args[0] if args else "192.168.0.100"
            cmd_text = " ".join(args[1:]) if len(args) >= 2 else "default command"
            return self.connect_scheduler_plc(ip, cmd_text)
        elif command == "rtu":
            ip = args[0] if args else "192.168.0.101"
            cmd_text = " ".join(args[1:]) if len(args) >= 2 else "default command"
            return self.connect_siemens_rtu(ip, cmd_text)
        elif command == "nmap":
            target = args[0] if args else "localhost"
            return self.nmap_scan(target)
        elif command == "speedtest":
            return self.speed_test()
        elif command == "record":
            return self.record_user_actions()
        elif command == "keyevent":
            return self.generate_keyboard_event()
        elif command == "mouseevent":
            return self.generate_mouse_event()
        elif command == "chrome":
            return self.start_chrome_dino()
        elif command == "telegramchat":
            message = " ".join(args) if args else "Hello, this is a chat message."
            return self.telegram_chat(message)
        elif command == "playfile":
            file_path = args[0] if args else ""
            return self.select_and_play_local_file(file_path)
        elif command == "webcam":
            return self.connect_webcam()
        elif command == "sudoku":
            return self.play_sudoku()
        elif command == "remotecommand":
            if len(args) >= 2:
                ip = args[0]
                cmd = " ".join(args[1:])
                return self.run_remote_command(ip, cmd)
            else:
                return "Insufficient parameters for remote command."
        elif command == "localcamera":
            return self.open_local_camera()
        elif command == "rs232":
            port = args[0] if args else "COM1"
            cmd = " ".join(args[1:]) if len(args) >= 2 else ""
            return self.rs232_comm(port, cmd)
        elif command == "osstate":
            return self.check_os_state()
        elif command == "ettercap":
            target = args[0] if args else "localhost"
            return self.ettercap_mirror(target)
        elif command == "googlemap":
            destination = " ".join(args) if args else "New York, NY"
            return self.google_map_direction(destination)
        elif command == "cytoscape":
            graph_file = args[0] if args else "graph_file.txt"
            return self.open_cytoscape(graph_file)
        elif command == "obfuscate":
            code = " ".join(args) if args else ""
            return self.obfuscate_python(code)
        elif command == "ftp_connect":
            if len(args) >= 3:
                ftp_server = args[0]
                username = args[1]
                password = args[2]
                return self.connect_ftp(ftp_server, username, password)
            else:
                return "Insufficient parameters for ftp_connect command."
        else:
            return "Command not recognized."
    
    def execute_employee_tasks(self):
        for emp in self.employees:
            name = emp.get("name", "Unknown")
            logging.info(f"Processing tasks for {name}")
            
            if "ping a remote host" in emp.get("workstation_functions", ""):
                self.ping_host(emp.get("ip_address", "8.8.8.8"))
            
            if "download all the contents in a web page" in emp.get("workstation_functions", ""):
                self.download_webpage("http://example.com")
            
            if "open an url using a browser" in emp.get("workstation_functions", ""):
                self.open_url("http://example.com")
            
            if "send telegram message" in emp.get("workstation_functions", ""):
                self.send_telegram_message("your_bot_token", "your_chat_id", f"Hello from {name}")
            
            if "run system commands" in emp.get("workstation_functions", ""):
                self.run_system_command("echo System Command Executed")
            
            if "open desktop application" in emp.get("workstation_functions", ""):
                self.open_application("C:\\Program Files\\Notepad++\\notepad++.exe")
            
            if "edit a powerpoint" in emp.get("workstation_functions", ""):
                self.edit_powerpoint("C:\\Work\\presentation.pptx", "Default update")
            
            if "clone a github repository" in emp.get("workstation_functions", ""):
                self.clone_github_repo("https://github.com/example/repo.git", "C:\\Projects\\repo")
            
            if "send and receive email" in emp.get("workstation_functions", ""):
                self.send_email("your_email@gmail.com", "recipient@example.com",
                                os.getenv("EMAIL_PASSWORD", ""), "Test Subject", "Test Body")
            
            if "connect to a remote host using ssh" in emp.get("workstation_functions", ""):
                output = self.connect_ssh(
                    emp.get("ip_address", "8.8.8.8"),
                    emp.get("ssh_username", "user"),
                    emp.get("ssh_password", "pass"),
                    "ls"
                )
                logging.info(f"SSH Output for {name}: {output}")
        return "Employee tasks executed."

if __name__ == "__main__":
    system = CUESystem()
    print("Executing employee tasks...")
    result = system.execute_employee_tasks()
    print(result)
