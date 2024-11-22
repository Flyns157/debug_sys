import unittest
import os
import tempfile
import shutil
from debug_sys.log_manager import LogManager

class TestLogManager(unittest.TestCase):
    def setUp(self):
        """
        Set up a temporary directory for test logs
        """
        self.test_dir = tempfile.mkdtemp()
        self.log_manager = LogManager()

    def tearDown(self):
        """
        Clean up temporary directory after tests
        """
        shutil.rmtree(self.test_dir)

    def test_add_logger(self):
        """
        Test adding a new logger
        """
        logger_name = 'test_logger'
        log_file = os.path.join(self.test_dir, 'test.log')
        
        # Add logger
        self.log_manager.add_logger(logger_name, log_file)
        
        # Check if logger exists
        self.assertIn(logger_name, self.log_manager.loggers)
        self.assertTrue(hasattr(self.log_manager, logger_name))

    def test_log_message(self):
        """
        Test logging a message
        """
        logger_name = 'test_logger'
        log_file = os.path.join(self.test_dir, 'test.log')
        
        # Add logger
        self.log_manager.add_logger(logger_name, log_file)
        
        # Log a message
        message = 'Test log message'
        self.log_manager.log(logger_name, 'INFO', message)
        
        # Check if log file exists and contains the message
        with open(log_file, 'r') as f:
            log_content = f.read()
            self.assertIn(message, log_content)

    def test_print_logs(self):
        """
        Test printing logs with a limit
        """
        logger_name = 'test_logger'
        log_file = os.path.join(self.test_dir, 'test.log')
        
        # Add logger
        self.log_manager.add_logger(logger_name, log_file)
        
        # Log multiple messages
        for i in range(10):
            self.log_manager.log(logger_name, 'INFO', f'Log message {i}')
        
        # Capture printed logs
        import io
        import sys
        captured_output = io.StringIO()
        sys.stdout = captured_output
        
        # Print last 5 logs
        self.log_manager.print_logs(logger_name, limit=5)
        
        # Restore stdout
        sys.stdout = sys.__stdout__
        
        # Check output
        output = captured_output.getvalue()
        self.assertEqual(output.count('Log message'), 5)

    def test_clear_logs(self):
        """
        Test clearing logs with archiving
        """
        logger_name = 'test_logger'
        log_file = os.path.join(self.test_dir, 'test.log')
        archive_dir = os.path.join(self.test_dir, 'archive')
        
        # Create archive directory
        os.makedirs(archive_dir)
        
        # Add logger
        self.log_manager.add_logger(logger_name, log_file)
        
        # Log messages
        for i in range(10):
            self.log_manager.log(logger_name, 'INFO', f'Log message {i}')
        
        # Clear logs with archiving
        self.log_manager.clear_logs(logger_name, archive=True, saving_folder=archive_dir)
        
        # Check log file is empty
        with open(log_file, 'r') as f:
            self.assertEqual(f.read().strip(), '')
        
        # Check archive file exists
        archive_files = os.listdir(archive_dir)
        self.assertEqual(len(archive_files), 1)

    def test_invalid_logger(self):
        """
        Test handling of invalid logger
        """
        with self.assertRaises(ValueError):
            self.log_manager.log('non_existent_logger', 'INFO', 'Test message')

if __name__ == '__main__':
    unittest.main()
